# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cipherUi.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QStatusBar,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class CipherUI(object):
    def setupUi(self, cipherWindow):
        if not cipherWindow.objectName():
            cipherWindow.setObjectName(u"cipherWindow")
        cipherWindow.resize(583, 394)
        self.actionSave = QAction(cipherWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_As = QAction(cipherWindow)
        self.actionSave_As.setObjectName(u"actionSave_As")
        self.actionOpen = QAction(cipherWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.centralwidget = QWidget(cipherWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.credentials = QTableWidget(self.centralwidget)
        if (self.credentials.columnCount() < 2):
            self.credentials.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.credentials.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.credentials.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.credentials.setObjectName(u"credentials")

        self.gridLayout.addWidget(self.credentials, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.envEdit = QLineEdit(self.centralwidget)
        self.envEdit.setObjectName(u"envEdit")

        self.verticalLayout.addWidget(self.envEdit)

        self.env2Edit = QLineEdit(self.centralwidget)
        self.env2Edit.setObjectName(u"env2Edit")

        self.verticalLayout.addWidget(self.env2Edit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pageEdit = QLineEdit(self.centralwidget)
        self.pageEdit.setObjectName(u"pageEdit")

        self.horizontalLayout.addWidget(self.pageEdit)

        self.passwordEdit = QLineEdit(self.centralwidget)
        self.passwordEdit.setObjectName(u"passwordEdit")

        self.horizontalLayout.addWidget(self.passwordEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.uppercaseCheck = QCheckBox(self.centralwidget)
        self.uppercaseCheck.setObjectName(u"uppercaseCheck")
        self.uppercaseCheck.setChecked(True)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.uppercaseCheck)

        self.lowercaseCheck = QCheckBox(self.centralwidget)
        self.lowercaseCheck.setObjectName(u"lowercaseCheck")
        self.lowercaseCheck.setChecked(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lowercaseCheck)

        self.digitsCheck = QCheckBox(self.centralwidget)
        self.digitsCheck.setObjectName(u"digitsCheck")
        self.digitsCheck.setChecked(True)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.digitsCheck)

        self.specialCheck = QCheckBox(self.centralwidget)
        self.specialCheck.setObjectName(u"specialCheck")
        self.specialCheck.setChecked(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.specialCheck)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.lengthSpin = QSpinBox(self.centralwidget)
        self.lengthSpin.setObjectName(u"lengthSpin")
        self.lengthSpin.setMinimum(2)
        self.lengthSpin.setMaximum(100)
        self.lengthSpin.setValue(16)

        self.horizontalLayout_3.addWidget(self.lengthSpin)


        self.formLayout.setLayout(3, QFormLayout.LabelRole, self.horizontalLayout_3)

        self.generateButton = QPushButton(self.centralwidget)
        self.generateButton.setObjectName(u"generateButton")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.generateButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(4, QFormLayout.FieldRole, self.verticalSpacer)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.addButton = QPushButton(self.centralwidget)
        self.addButton.setObjectName(u"addButton")

        self.horizontalLayout_2.addWidget(self.addButton)

        self.updateButton = QPushButton(self.centralwidget)
        self.updateButton.setObjectName(u"updateButton")
        self.updateButton.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.updateButton)

        self.deleteButton = QPushButton(self.centralwidget)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.deleteButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.visibleCheck = QCheckBox(self.centralwidget)
        self.visibleCheck.setObjectName(u"visibleCheck")
        self.visibleCheck.setChecked(True)

        self.verticalLayout.addWidget(self.visibleCheck)


        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)

        cipherWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(cipherWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 583, 25))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        cipherWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(cipherWindow)
        self.statusbar.setObjectName(u"statusbar")
        cipherWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)

        self.retranslateUi(cipherWindow)

        QMetaObject.connectSlotsByName(cipherWindow)
    # setupUi

    def retranslateUi(self, cipherWindow):
        cipherWindow.setWindowTitle(QCoreApplication.translate("cipherWindow", u"Cipher", None))
        self.actionSave.setText(QCoreApplication.translate("cipherWindow", u"Save", None))
        self.actionSave_As.setText(QCoreApplication.translate("cipherWindow", u"Save As...", None))
        self.actionOpen.setText(QCoreApplication.translate("cipherWindow", u"Open", None))
        ___qtablewidgetitem = self.credentials.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("cipherWindow", u"Page", None));
        ___qtablewidgetitem1 = self.credentials.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("cipherWindow", u"Password", None));
        self.envEdit.setText("")
        self.envEdit.setPlaceholderText(QCoreApplication.translate("cipherWindow", u"Env", None))
        self.env2Edit.setText("")
        self.env2Edit.setPlaceholderText(QCoreApplication.translate("cipherWindow", u"Env2", None))
        self.pageEdit.setPlaceholderText(QCoreApplication.translate("cipherWindow", u"Page", None))
        self.passwordEdit.setPlaceholderText(QCoreApplication.translate("cipherWindow", u"Password", None))
        self.label.setText(QCoreApplication.translate("cipherWindow", u"Characters:", None))
        self.uppercaseCheck.setText(QCoreApplication.translate("cipherWindow", u"Uppercase", None))
        self.lowercaseCheck.setText(QCoreApplication.translate("cipherWindow", u"Lowercase", None))
        self.digitsCheck.setText(QCoreApplication.translate("cipherWindow", u"Digits", None))
        self.specialCheck.setText(QCoreApplication.translate("cipherWindow", u"Special", None))
        self.label_2.setText(QCoreApplication.translate("cipherWindow", u"Length:", None))
        self.generateButton.setText(QCoreApplication.translate("cipherWindow", u"Generate", None))
        self.addButton.setText(QCoreApplication.translate("cipherWindow", u"Add", None))
        self.updateButton.setText(QCoreApplication.translate("cipherWindow", u"Update", None))
        self.deleteButton.setText(QCoreApplication.translate("cipherWindow", u"Delete", None))
        self.visibleCheck.setText(QCoreApplication.translate("cipherWindow", u"Visible", None))
        self.menuFile.setTitle(QCoreApplication.translate("cipherWindow", u"File", None))
    # retranslateUi

