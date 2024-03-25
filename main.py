from PySide6.QtWidgets import QApplication, QDialog, QFileDialog, QColorDialog, QMessageBox
from window import Ui_Dialog
from PySide6.QtCore import QThread
from processing_files import Worker0
from PySide6.QtGui import QIcon
from functools import partial

import resources_rc


class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.colors = {}
        self.isProcessing = False
        self.text_contents = None
        self.file_paths = None
        self.worker = None
        self.thread = None
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.initialize_ui_states()
        self.connect_signals()

    def initialize_ui_states(self):
        self.ui.process_tab0.setEnabled(False)
        self.file_paths = {'xlsx': None, 'pdf': None}
        self.text_contents = {'pattern': 'ID', 'suffix': ',', 'prefix': ' test: '}
        excel_widgets = [self.ui.excel_file_tab0, self.ui.excel1_file_tab1, self.ui.excel2_file_tab1]
        pdf_widgets = [self.ui.pdf_file_tab0]
        for widget in excel_widgets:
            widget.mousePressEvent = self.open_excel_file_dialog
            widget.addItem("Click to select an Excel file...")
        for widget in pdf_widgets:
            widget.mousePressEvent = self.open_pdf_file_dialog
            widget.addItem("Click to select a PDF file...")
        self.ui.prefix_1_tab0.setPlainText(self.text_contents['prefix'])
        self.ui.pattern_1_tab0.setPlainText(self.text_contents['pattern'])
        self.ui.suffix_1_tab0.setPlainText(self.text_contents['suffix'])
        self.setup_checkboxes_and_buttons()

    def setup_checkboxes_and_buttons(self):
        if hasattr(self.ui, 'color_1_tab0') and self.ui.color_1_tab0 is not None:
            button = self.ui.color_1_tab0
            button.clicked.connect(partial(self.change_button_color, button))
        if hasattr(self.ui, 'color_1_tab1') and self.ui.color_1_tab1 is not None:
            button = self.ui.color_1_tab1
            button.clicked.connect(partial(self.change_button_color, button))

    def change_button_color(self, button):
        color = QColorDialog.getColor()
        if color.isValid():
            hex_color = color.name()
            button.setStyleSheet(f'background-color: {hex_color}')
            self.colors[button.objectName()] = hex_color
            self.check_fields_filled0()

    def connect_signals(self):
        for attr in ('pattern', 'suffix', 'prefix'):
            widget = self.ui.__getattribute__(f'{attr}_1_tab0')
            widget.textChanged.connect(getattr(self, f'update_{attr}'))
            widget.textChanged.connect(self.check_fields_filled0)
        self.ui.process_tab0.clicked.connect(self.process_files0)
        self.ui.process_tab1.clicked.connect(self.process_files1)

    def update_attribute_from_ui(self, attribute_name, ui_element):
        setattr(self, attribute_name, ui_element.toPlainText())

    def update_pattern(self):
        self.update_attribute_from_ui('pattern_text', self.ui.pattern_1_tab0)

    def update_suffix(self):
        self.update_attribute_from_ui('suffix_text', self.ui.suffix_1_tab0)

    def update_prefix(self):
        self.update_attribute_from_ui('prefix_text', self.ui.prefix_1_tab0)

    def open_excel_file_dialog(self, event):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open Excel File", "", "Excel Files (*.xls *.xlsx)")
        if filePath:
            fileName = filePath.split("/")[-1]
            self.ui.excel_file_tab0.clear()
            self.ui.excel_file_tab0.addItem(fileName)
            self.file_paths['xlsx'] = filePath
            self.check_fields_filled0()

    def open_pdf_file_dialog(self, event):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open PDF File", "", "PDF Files (*.pdf)")
        if filePath:
            fileName = filePath.split("/")[-1]
            self.ui.pdf_file_tab0.clear()
            self.ui.pdf_file_tab0.addItem(fileName)
            self.file_paths['pdf'] = filePath
            self.check_fields_filled0()

    def process_files1(self):
        self.setEnabled(True)
        self.ui.process_tab0.setEnabled(True)
        QMessageBox.information(self, "Not Implemented", "Not Implemented")
        self.check_fields_filled0()

    def process_files0(self):
        # Check for ongoing processing
        if self.isProcessing:
            QMessageBox.warning(self, "Processing", "Please wait for the current processing to complete.")
            return  # Exit the method to prevent starting a new process

        # Prepare the data for processing
        data_to_process = [{
            'prefix': self.ui.prefix_1_tab0.toPlainText(),
            'pattern': self.ui.pattern_1_tab0.toPlainText(),
            'suffix': self.ui.suffix_1_tab0.toPlainText(),
            'color': self.colors.get('color_1_tab0', '#FFFFFF')
        }]

        self.isProcessing = True  # Set the flag when starting a new process
        self.thread = QThread()  # Create a new thread
        self.worker = Worker0(self.file_paths['xlsx'], self.file_paths['pdf'], data_to_process)  # Create a new worker
        self.worker.moveToThread(self.thread)

        # Connect signals and slots
        self.thread.started.connect(self.worker.process)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.on_processing_finished)
        # Update the flag and UI when the process is finished
        self.worker.finished.connect(lambda: setattr(self, 'isProcessing', False))
        self.worker.finished.connect(lambda: self.ui.process_tab0.setEnabled(True))
        self.worker.finished.connect(lambda: self.setEnabled(True))
        # Schedule the worker and thread for deletion
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()
        self.ui.process_tab0.setEnabled(False)
        self.setEnabled(False)

        # Show a progress dialog
        self.progressDialog = QMessageBox(self)
        self.progressDialog.setWindowTitle("Processing")
        self.progressDialog.setText("Processing, please wait...")
        self.progressDialog.setStandardButtons(QMessageBox.NoButton)
        self.progressDialog.show()

    def on_processing_finished(self):
        self.progressDialog.accept()
        self.setEnabled(True)
        self.ui.process_tab0.setEnabled(True)
        QMessageBox.information(self, "Processing Complete", "The processing has been completed.")

    def check_fields_filled0(self):
        excel_file_selected = self.file_paths['xlsx'] is not None
        pdf_file_selected = self.file_paths['pdf'] is not None
        fields_filled = self.are_fields_filled_for_checkbox(1)
        all_conditions_met = excel_file_selected and pdf_file_selected and fields_filled
        self.ui.process_tab0.setEnabled(all_conditions_met)

    def are_fields_filled_for_checkbox(self, index):
        pattern_filled = self.ui.pattern_1_tab0.toPlainText() != ""
        color_chosen = self.colors.get('color_1_tab0') is not None  # Check if color is chosen from self.colors
        return pattern_filled and color_chosen

    def closeEvent(self, event):
        if self.isProcessing:  # Check if processing is ongoing
            reply = QMessageBox.question(self, 'Processing',
                                         "A process is still running. Are you sure you want to quit?",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                if self.thread:  # Safely attempt to stop the thread if it exists
                    self.worker.stop()  # Ensure this method exists in your worker to stop processing
                    self.thread.quit()
                    self.thread.wait(2000)  # Wait for a maximum of 2000 milliseconds for the thread to finish
                event.accept()  # Accept the close event
            else:
                event.ignore()  # Ignore the close event, keeping the application open
        else:
            event.accept()  # No processing is active, safe to close


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(":/icon"))
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
