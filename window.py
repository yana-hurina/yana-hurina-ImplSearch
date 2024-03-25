# -*- coding: utf-8 -*-

################################################################################
#  Form generated from reading UI file 'window.ui'
##
#  Created by: Qt User Interface Compiler version 6.6.2
##
#  WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QCheckBox, QComboBox,
                               QGridLayout, QHBoxLayout, QLabel, QPushButton,
                               QSizePolicy, QTabWidget, QTextEdit, QWidget)


class Ui_Dialog(object):
    def __init__(self):
        self.tab_1 = None
        self.excel_file_tab0 = None
        self.pdf_file_tab0 = None

        self.prefix_1_tab0 = None
        self.pattern_1_tab0 = None
        self.suffix_1_tab0 = None
        self.color_1_tab0 = None

        self.process_tab0 = None

        self.excel1_file_tab1 = None
        self.excel2_file_tab1 = None

        self.prefix_1_tab1 = None
        self.pattern_1_tab1 = None
        self.suffix_1_tab1 = None
        self.color_1_tab1 = None
        self.match_1_tab1 = None

        self.process_tab1 = None

    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(720, 180)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(720, 180))
        Dialog.setMaximumSize(QSize(720, 200))
        self.gridLayout_2 = QGridLayout(Dialog)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.gridLayout = QGridLayout(self.tab_1)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.tab_1)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMinimumSize(QSize(110, 25))
        self.label_2.setMaximumSize(QSize(16777215, 16777215))
        self.label_2.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.pdf_file_tab0 = QComboBox(self.tab_1)
        self.pdf_file_tab0.setObjectName(u"pdf_file_tab0")
        self.pdf_file_tab0.setMinimumSize(QSize(0, 25))
        font = QFont()
        font.setStyleStrategy(QFont.PreferAntialias)
        self.pdf_file_tab0.setFont(font)

        self.horizontalLayout_2.addWidget(self.pdf_file_tab0)

        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.process_tab0 = QPushButton(self.tab_1)
        self.process_tab0.setObjectName(u"process_tab0")
        self.process_tab0.setFocusPolicy(Qt.NoFocus)

        self.gridLayout.addWidget(self.process_tab0, 4, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.tab_1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 0))
        self.label_4.setMaximumSize(QSize(16777215, 16777215))
        self.label_4.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.prefix_1_tab0 = QTextEdit(self.tab_1)
        self.prefix_1_tab0.setObjectName(u"prefix_1_tab0")
        self.prefix_1_tab0.setMinimumSize(QSize(80, 25))
        self.prefix_1_tab0.setMaximumSize(QSize(16777215, 25))
        self.prefix_1_tab0.setFont(font)
        self.prefix_1_tab0.setFocusPolicy(Qt.ClickFocus)
        self.prefix_1_tab0.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.prefix_1_tab0.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_3.addWidget(self.prefix_1_tab0)

        self.label_6 = QLabel(self.tab_1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 0))
        self.label_6.setMaximumSize(QSize(16777215, 16777215))
        self.label_6.setLayoutDirection(Qt.LeftToRight)
        self.label_6.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_6)

        self.pattern_1_tab0 = QTextEdit(self.tab_1)
        self.pattern_1_tab0.setObjectName(u"pattern_1_tab0")
        self.pattern_1_tab0.setMinimumSize(QSize(80, 25))
        self.pattern_1_tab0.setMaximumSize(QSize(16777215, 25))
        self.pattern_1_tab0.setFont(font)
        self.pattern_1_tab0.setFocusPolicy(Qt.ClickFocus)
        self.pattern_1_tab0.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.pattern_1_tab0.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_3.addWidget(self.pattern_1_tab0)

        self.label_5 = QLabel(self.tab_1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 0))
        self.label_5.setMaximumSize(QSize(16777215, 16777215))
        self.label_5.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_5)

        self.suffix_1_tab0 = QTextEdit(self.tab_1)
        self.suffix_1_tab0.setObjectName(u"suffix_1_tab0")
        self.suffix_1_tab0.setMinimumSize(QSize(80, 25))
        self.suffix_1_tab0.setMaximumSize(QSize(16777215, 25))
        self.suffix_1_tab0.setFont(font)
        self.suffix_1_tab0.setFocusPolicy(Qt.ClickFocus)
        self.suffix_1_tab0.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.suffix_1_tab0.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_3.addWidget(self.suffix_1_tab0)

        self.color_1_tab0 = QPushButton(self.tab_1)
        self.color_1_tab0.setObjectName(u"color_1_tab0")
        self.color_1_tab0.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_3.addWidget(self.color_1_tab0)

        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.tab_1)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(110, 25))
        self.label.setMaximumSize(QSize(16777215, 16777215))
        self.label.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label)

        self.excel_file_tab0 = QComboBox(self.tab_1)
        self.excel_file_tab0.setObjectName(u"excel_file_tab0")
        self.excel_file_tab0.setMinimumSize(QSize(0, 25))
        self.excel_file_tab0.setFont(font)

        self.horizontalLayout.addWidget(self.excel_file_tab0)

        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_15 = QLabel(self.tab_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(0, 0))
        self.label_15.setMaximumSize(QSize(16777215, 16777215))
        self.label_15.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_15)

        self.prefix_1_tab1 = QTextEdit(self.tab_2)
        self.prefix_1_tab1.setObjectName(u"prefix_1_tab1")
        self.prefix_1_tab1.setMinimumSize(QSize(80, 25))
        self.prefix_1_tab1.setMaximumSize(QSize(16777215, 25))
        self.prefix_1_tab1.setFont(font)
        self.prefix_1_tab1.setFocusPolicy(Qt.ClickFocus)
        self.prefix_1_tab1.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.prefix_1_tab1.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_9.addWidget(self.prefix_1_tab1)

        self.label_14 = QLabel(self.tab_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 0))
        self.label_14.setMaximumSize(QSize(16777215, 16777215))
        self.label_14.setLayoutDirection(Qt.LeftToRight)
        self.label_14.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_14)

        self.pattern_1_tab1 = QTextEdit(self.tab_2)
        self.pattern_1_tab1.setObjectName(u"pattern_1_tab1")
        self.pattern_1_tab1.setMinimumSize(QSize(80, 25))
        self.pattern_1_tab1.setMaximumSize(QSize(16777215, 25))
        self.pattern_1_tab1.setFont(font)
        self.pattern_1_tab1.setFocusPolicy(Qt.ClickFocus)
        self.pattern_1_tab1.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.pattern_1_tab1.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_9.addWidget(self.pattern_1_tab1)

        self.label_16 = QLabel(self.tab_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(0, 0))
        self.label_16.setMaximumSize(QSize(16777215, 16777215))
        self.label_16.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_16)

        self.suffix_1_tab1 = QTextEdit(self.tab_2)
        self.suffix_1_tab1.setObjectName(u"suffix_1_tab1")
        self.suffix_1_tab1.setMinimumSize(QSize(80, 25))
        self.suffix_1_tab1.setMaximumSize(QSize(16777215, 25))
        self.suffix_1_tab1.setFont(font)
        self.suffix_1_tab1.setFocusPolicy(Qt.ClickFocus)
        self.suffix_1_tab1.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.suffix_1_tab1.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_9.addWidget(self.suffix_1_tab1)

        self.match_1_tab1 = QCheckBox(self.tab_2)
        self.match_1_tab1.setObjectName(u"match_1_tab1")

        self.horizontalLayout_9.addWidget(self.match_1_tab1)

        self.color_1_tab1 = QPushButton(self.tab_2)
        self.color_1_tab1.setObjectName(u"color_1_tab1")
        self.color_1_tab1.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_9.addWidget(self.color_1_tab1)

        self.gridLayout_3.addLayout(self.horizontalLayout_9, 2, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_13 = QLabel(self.tab_2)
        self.label_13.setObjectName(u"label_13")
        sizePolicy1.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy1)
        self.label_13.setMinimumSize(QSize(110, 25))
        self.label_13.setMaximumSize(QSize(16777215, 16777215))
        self.label_13.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_13)

        self.excel2_file_tab1 = QComboBox(self.tab_2)
        self.excel2_file_tab1.setObjectName(u"excel2_file_tab1")
        self.excel2_file_tab1.setMinimumSize(QSize(0, 25))
        self.excel2_file_tab1.setFont(font)

        self.horizontalLayout_8.addWidget(self.excel2_file_tab1)

        self.gridLayout_3.addLayout(self.horizontalLayout_8, 1, 0, 1, 1)

        self.process_tab1 = QPushButton(self.tab_2)
        self.process_tab1.setObjectName(u"process_tab1")
        self.process_tab1.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_3.addWidget(self.process_tab1, 3, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_12 = QLabel(self.tab_2)
        self.label_12.setObjectName(u"label_12")
        sizePolicy1.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy1)
        self.label_12.setMinimumSize(QSize(110, 25))
        self.label_12.setMaximumSize(QSize(16777215, 16777215))
        self.label_12.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_12)

        self.excel1_file_tab1 = QComboBox(self.tab_2)
        self.excel1_file_tab1.setObjectName(u"excel1_file_tab1")
        self.excel1_file_tab1.setMinimumSize(QSize(0, 25))
        self.excel1_file_tab1.setFont(font)

        self.horizontalLayout_7.addWidget(self.excel1_file_tab1)

        self.gridLayout_3.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"ImplSearch", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"PDF comparison:", None))
        self.process_tab0.setText(QCoreApplication.translate("Dialog", u"PROCESS", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Prefix Pattern:", None))
        # if QT_CONFIG(tooltip)
        self.prefix_1_tab0.setToolTip(QCoreApplication.translate("Dialog",
                                                                 u"Enter any text or characters that come directly before the search term",
                                                                 None))
        # endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Search For:", None))
        # if QT_CONFIG(tooltip)
        self.pattern_1_tab0.setToolTip(
            QCoreApplication.translate("Dialog", u"Enter the term you are searching for (e.g., ID, NAME)", None))
        # endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Suffix Pattern:", None))
        # if QT_CONFIG(tooltip)
        self.suffix_1_tab0.setToolTip(QCoreApplication.translate("Dialog",
                                                                 u"Enter any text or characters that come directly after the search term",
                                                                 None))
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(tooltip)
        self.color_1_tab0.setToolTip(
            QCoreApplication.translate("Dialog", u"Color to highlight found item in output document", None))
        # endif // QT_CONFIG(tooltip)
        self.color_1_tab0.setText(QCoreApplication.translate("Dialog", u"Choose Color", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Excel:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1),
                                  QCoreApplication.translate("Dialog", u"Excel_PDF", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"Prefix Pattern:", None))
        # if QT_CONFIG(tooltip)
        self.prefix_1_tab1.setToolTip(QCoreApplication.translate("Dialog",
                                                                 u"Enter any text or characters that come directly before the search term",
                                                                 None))
        # endif // QT_CONFIG(tooltip)
        self.label_14.setText(QCoreApplication.translate("Dialog", u"Search For:", None))
        # if QT_CONFIG(tooltip)
        self.pattern_1_tab1.setToolTip(
            QCoreApplication.translate("Dialog", u"Enter the term you are searching for (e.g., ID, NAME)", None))
        # endif // QT_CONFIG(tooltip)
        self.label_16.setText(QCoreApplication.translate("Dialog", u"Suffix Pattern:", None))
        # if QT_CONFIG(tooltip)
        self.suffix_1_tab1.setToolTip(QCoreApplication.translate("Dialog",
                                                                 u"Enter any text or characters that come directly after the search term",
                                                                 None))
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(tooltip)
        self.match_1_tab1.setToolTip(
            QCoreApplication.translate("Dialog", u"Check to search cell that contains only searched item", None))
        # endif // QT_CONFIG(tooltip)
        self.match_1_tab1.setText(QCoreApplication.translate("Dialog", u"exact match", None))
        # if QT_CONFIG(tooltip)
        self.color_1_tab1.setToolTip(
            QCoreApplication.translate("Dialog", u"Color to highlight found item in output document", None))
        # endif // QT_CONFIG(tooltip)
        self.color_1_tab1.setText(QCoreApplication.translate("Dialog", u"Choose Color", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"Excel 2 to search in:", None))
        self.process_tab1.setText(QCoreApplication.translate("Dialog", u"PROCESS", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"Excel:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2),
                                  QCoreApplication.translate("Dialog", u"Excel_Excel", None))
    # retranslateUi
