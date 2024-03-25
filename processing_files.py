import os
from PySide6.QtCore import QObject, Signal
from read_excel import ExcelProcessor
from read_pdf import PDFSearcher
from update_excel import ExcelHyperlinkUpdater


class Worker0(QObject):
    finished = Signal()
    progress = Signal(int)

    # Updated __init__ to accept a single data list instead of individual attributes
    def __init__(self, file_xlsx_path, file_pdf_path, data, parent=None):
        super().__init__(parent)
        self._running = True  # Add a running flag
        self.file_xlsx_path = file_xlsx_path
        self.file_pdf_path = file_pdf_path
        self.data = data
        # print(f"self.data {self.data}")

    def process(self):
        for entry in self.data:
            pattern_text = entry['pattern']
            suffix_text = entry['suffix']
            prefix_text = entry['prefix']
            colour = entry['color']

            # Initialize the processor with current dataset and process Excel
            processor = ExcelProcessor(self.file_xlsx_path, pattern_text)
            result = processor.process_excel()

            # Initialize PDFSearcher with the current static prefix and suffix
            pdf_searcher = PDFSearcher(self.file_pdf_path, prefix_text, suffix_text)

            # Pass the result from Excel processing to search_in_pdf
            found_data = pdf_searcher.search_in_pdf(result)

            # Perform the necessary updates for each dataset
            # Extract the directory and filename without extension for this dataset
            directory, filename = os.path.split(self.file_xlsx_path)
            basename, extension = os.path.splitext(filename)

            # Construct a new filename for the updated Excel file for this dataset
            copy_file_xlsx = os.path.join(directory, f"{basename}_updated_with_{pattern_text}.xlsx")

            # Use the updater to copy and update the Excel file with the found data
            updater = ExcelHyperlinkUpdater(self.file_xlsx_path, colour)
            updater.copy_and_update_excel(found_data, copy_file_xlsx)

        # Signal that processing for all datasets is complete
        self.finished.emit()

    def stop(self):
        self._running = False  # Assume you have a _running attribute controlling the loop
