import gui, os, file, password
from PySide6.QtWidgets import QMainWindow, QFileDialog, QTableWidgetItem, QLineEdit, QStyledItemDelegate, QStyle, QApplication, QMessageBox
from PySide6.QtCore import Qt

class PasswordDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)
        style = option.widget.style() or QApplication.style()
        hint = style.styleHint(QStyle.SH_LineEdit_PasswordCharacter)
        option.text = chr(hint) * len(option.text)



class CipherWindow(QMainWindow):
    def __init__(self, app):
        self._file = file.File()
        self._pass = password.Password()
        super(CipherWindow, self).__init__()
        self._ui = gui.CipherUI()
        self._ui.setupUi(self)
        self._ui.actionSave_As.triggered.connect(self.saveAs)
        self._ui.actionSave.triggered.connect(self.save)
        self._ui.actionOpen.triggered.connect(self.load)
        self._ui.envEdit.textChanged.connect(self.fileEnvChanged)
        self._ui.env2Edit.textChanged.connect(self.decodeEnvChanged)
        self._ui.pageEdit.textChanged.connect(self.credentialsEdited)
        self._ui.passwordEdit.textChanged.connect(self.credentialsEdited)
        self._ui.passwordEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self._ui.envEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self._ui.env2Edit.setEchoMode(QLineEdit.EchoMode.Password)
        self._ui.visibleCheck.setChecked(False)
        self._ui.visibleCheck.stateChanged.connect(self.visibilityChanged)
        self._ui.uppercaseCheck.stateChanged.connect(self.uppercaseChanged)
        self._ui.lowercaseCheck.stateChanged.connect(self.lowercaseChanged)
        self._ui.digitsCheck.stateChanged.connect(self.digitsChanged)
        self._ui.specialCheck.stateChanged.connect(self.specialChanged)
        self._ui.generateButton.clicked.connect(self.generate)
        self._ui.lengthSpin.valueChanged.connect(self.lengthChanged)
        self._delegate = PasswordDelegate()
        self._ui.credentials.setItemDelegateForColumn(1, self._delegate)
        self.toogleButtons(False, False, False)
        self._ui.addButton.clicked.connect(self.add)
        self._ui.updateButton.clicked.connect(self.update)
        self._ui.deleteButton.clicked.connect(self.delete)
        self._ui.credentials.cellClicked.connect(self.selectItem)
        self._ui.credentials.cellDoubleClicked.connect(self.copyToClipboard)
        self._app = app
        self._selectedRow = None
        self._selectedItem = None
    
    def load(self) -> None:
        fileName = QFileDialog.getOpenFileName(self, u"Open file", os.getcwd(), "Password (*.pd)")[0]
        previousPath = self._file.path
        self._file.path = fileName
        try:
            self._file.decode()
            self._ui.credentials.clear()
            self._ui.credentials.setRowCount(len(self._file.data.keys()))
            self._ui.credentials.setColumnCount(2)
            self._ui.credentials.setHorizontalHeaderLabels(["Page", "Password"])
            for index, (site, password) in enumerate(self._file.data.items()):
                self.insertRow(index, site, password)
        except:
            self._file.path = previousPath
            QMessageBox.information(self, "Incorrect file", "Failed to read file content!")
        
    def saveAs(self) -> None:
        if self.edited:
            fileName = QFileDialog.getSaveFileName(self, u"Save file", os.getcwd(), "Password (*.pd)")[0]
            self._file.path = fileName
            self.saveFile()

    def save(self) -> None:
        if not self._file:
            self.saveAs()
            return
        if self.edited:
            self.saveFile()

    def saveFile(self) -> None:
        self._file.encode()


    def fileEnvChanged(self, text: str) -> None:
        self._file.file_key = text
    
    def decodeEnvChanged(self, text: str) -> None:
        self._file.decode_key = text
    
    def visibilityChanged(self, state: bool) -> None:
        if state:
            self._ui.passwordEdit.setEchoMode(QLineEdit.EchoMode.Normal)
            self._ui.envEdit.setEchoMode(QLineEdit.EchoMode.Normal)
            self._ui.env2Edit.setEchoMode(QLineEdit.EchoMode.Normal)
            return
        self._ui.passwordEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self._ui.envEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self._ui.env2Edit.setEchoMode(QLineEdit.EchoMode.Password)
    
    def uppercaseChanged(self, state: bool) -> None:
        self._pass.uppercase = state


    def lowercaseChanged(self, state: bool) -> None:
        self._pass.lowercase = state

    def digitsChanged(self, state: bool) -> None:
        self._pass.digits = state

    def specialChanged(self, state: bool) -> None:
        self._pass.specialChars = state

    def lengthChanged(self, value: int) -> None:
        self._pass.length = value

    def selectItem(self, row: int, col: int) -> None:
        self._selectedItem = self._ui.credentials.item(row, 0).text()
        self._ui.pageEdit.setText(self._selectedItem) 
        self._ui.passwordEdit.setText(self._ui.credentials.item(row, 1).text())
        self._selectedRow = row
        self.toogleButtons(False, False, True)

    def copyToClipboard(self, row: int, col: int) -> None:
        clipboard = self._app.clipboard()
        clipboard.clear(mode=clipboard.Clipboard)
        clipboard.setText(self._ui.credentials.item(row, 1).text())

    def toogleButtons(self, add: bool, update: bool, delete: bool) -> None:
        self._ui.addButton.setEnabled(add)
        self._ui.updateButton.setEnabled(update)
        self._ui.deleteButton.setEnabled(delete)
    
    def credentialsEdited(self) -> None:
        key = self._ui.pageEdit.text()
        password = self._ui.passwordEdit.text()
        if key == "" or password == "":
            self.toogleButtons(False, False, False)
            return
        if self._file.data.__contains__(key):
            if self._file.data[key] == password:
                self.toogleButtons(False, False, True)
                return
            else:
                self.toogleButtons(False, True, True)
                return
        self.toogleButtons(True, False, False)

    def insertRow(self, row: int, page: str, password: str) -> None:
        siteItem = QTableWidgetItem(page)
        passwordItem = QTableWidgetItem(password)
        passwordItem.setFlags(passwordItem.flags() &~ Qt.ItemIsEnabled)
        siteItem.setFlags(siteItem.flags() &~ Qt.ItemIsEditable)
        self._ui.credentials.setItem(row, 0, siteItem)
        self._ui.credentials.setItem(row, 1, passwordItem)

    def delete(self) -> None:
        self._ui.credentials.removeRow(self._selectedRow)
        self._file.data.pop(self._selectedItem)
        self._ui.passwordEdit.clear()
        self._ui.pageEdit.clear()
        self.toogleButtons(False, False, False)
        self._file.edited = True
    
    def update(self) -> None:
        password = self._ui.passwordEdit.text()
        self.insertRow(self._selectedRow, self._selectedItem, password)
        self._file.data.update({self._selectedItem: password})
        self.toogleButtons(False, False, True)
        self._file.edited = True

    def add(self) -> None:
        password = self._ui.passwordEdit.text()
        self._selectedItem = self._ui.pageEdit.text()
        self._selectedRow = len(self._file.data.keys())
        self._ui.credentials.setRowCount(self._selectedRow + 1)
        self.insertRow(self._selectedRow, self._selectedItem, password)
        self._file.data[self._selectedItem] = password
        self.toogleButtons(False, False, True)
        self._file.edited = True
    
    def generate(self) -> None:
        password = self._pass.generate()
        self._ui.passwordEdit.setText(password)



        
