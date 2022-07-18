import gui
import os
import file
import password
from PySide6.QtWidgets import (QMainWindow, QFileDialog, 
                               QTableWidgetItem, QLineEdit, QStyledItemDelegate, 
                               QStyle, QApplication, QMessageBox)
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
        self._ui.actionSave_As.triggered.connect(self.save_as)
        self._ui.actionSave.triggered.connect(self.save)
        self._ui.actionOpen.triggered.connect(self.load)
        self._ui.envEdit.textChanged.connect(self.file_env_changed)
        self._ui.env2Edit.textChanged.connect(self.decode_env_changed)
        self._ui.pageEdit.textChanged.connect(self.credentials_edited)
        self._ui.passwordEdit.textChanged.connect(self.credentials_edited)
        self._ui.passwordEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self._ui.envEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self._ui.env2Edit.setEchoMode(QLineEdit.EchoMode.Password)
        self._ui.visibleCheck.setChecked(False)
        self._ui.visibleCheck.stateChanged.connect(self.visibility_changed)
        self._ui.uppercaseCheck.stateChanged.connect(self.uppercase_changed)
        self._ui.lowercaseCheck.stateChanged.connect(self.lowercase_changed)
        self._ui.digitsCheck.stateChanged.connect(self.digits_changed)
        self._ui.specialCheck.stateChanged.connect(self.special_changed)
        self._ui.generateButton.clicked.connect(self.generate)
        self._ui.lengthSpin.valueChanged.connect(self.length_changed)
        self._delegate = PasswordDelegate()
        self._ui.credentials.setItemDelegateForColumn(1, self._delegate)
        self.toogle_buttons(False, False, False)
        self._ui.addButton.clicked.connect(self.add)
        self._ui.updateButton.clicked.connect(self.update)
        self._ui.deleteButton.clicked.connect(self.delete)
        self._ui.credentials.cellClicked.connect(self.select_item)
        self._ui.credentials.cellDoubleClicked.connect(self.copy_to_clipboard)
        self._app = app
        self._selected_row = None
        self._selected_item = None

    def load(self) -> None:
        file_name = QFileDialog.getOpenFileName(
            self, u"Open file", os.getcwd(), "Password (*.pd)")[0]
        previous_path = self._file.path
        self._file.path = file_name
        try:
            self._file.decode()
            self._ui.credentials.clear()
            self._ui.credentials.setRowCount(len(self._file.data.keys()))
            self._ui.credentials.setColumnCount(2)
            self._ui.credentials.setHorizontalHeaderLabels(
                ["Page", "Password"])
            for index, (site, pwd) in enumerate(self._file.data.items()):
                self.insert_row(index, site, pwd)
        except FileNotFoundError:
            self._file.path = previous_path
            QMessageBox.information(
                self, "Incorrect file", "Failed to read file content!")

    def save_as(self) -> None:
        if self.edited:
            file_name = QFileDialog.getSaveFileName(
                self, "Save file", os.getcwd(), "Password (*.pd)")[0]
            self._file.path = file_name
            self.save_file()

    def save(self) -> None:
        if not self._file:
            self.save_as()
            return
        if self.edited:
            self.save_file()

    def save_file(self) -> None:
        self._file.encode()

    def file_env_changed(self, text: str) -> None:
        self._file.file_key = text

    def decode_env_changed(self, text: str) -> None:
        self._file.decode_key = text

    def visibility_changed(self, state: bool) -> None:
        if state:
            self._ui.passwordEdit.setEchoMode(QLineEdit.EchoMode.Normal)
            self._ui.envEdit.setEchoMode(QLineEdit.EchoMode.Normal)
            self._ui.env2Edit.setEchoMode(QLineEdit.EchoMode.Normal)
            return
        self._ui.passwordEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self._ui.envEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self._ui.env2Edit.setEchoMode(QLineEdit.EchoMode.Password)

    def uppercase_changed(self, state: bool) -> None:
        self._pass.uppercase = state

    def lowercase_changed(self, state: bool) -> None:
        self._pass.lowercase = state

    def digits_changed(self, state: bool) -> None:
        self._pass.digits = state

    def special_changed(self, state: bool) -> None:
        self._pass.specialChars = state

    def length_changed(self, value: int) -> None:
        self._pass.length = value

    def select_item(self, row: int, col: int) -> None:
        self._selected_item = self._ui.credentials.item(row, 0).text()
        self._ui.pageEdit.setText(self._selected_item)
        self._ui.passwordEdit.setText(self._ui.credentials.item(row, 1).text())
        self._selected_row = row
        self.toogle_buttons(False, False, True)

    def copy_to_clipboard(self, row: int, col: int) -> None:
        clipboard = self._app.clipboard()
        clipboard.clear(mode=clipboard.Clipboard)
        clipboard.setText(self._ui.credentials.item(row, 1).text())

    def toogle_buttons(self, add: bool, update: bool, delete: bool) -> None:
        self._ui.addButton.setEnabled(add)
        self._ui.updateButton.setEnabled(update)
        self._ui.deleteButton.setEnabled(delete)

    def credentials_edited(self) -> None:
        key = self._ui.pageEdit.text()
        pwd = self._ui.passwordEdit.text()
        if key == "" or pwd == "":
            self.toogle_buttons(False, False, False)
            return
        if key in self._file.data:
            if self._file.data[key] == pwd:
                self.toogle_buttons(False, False, True)
                return
            else:
                self.toogle_buttons(False, True, True)
                return
        self.toogle_buttons(True, False, False)

    def insert_row(self, row: int, page: str, pwd: str) -> None:
        siteItem = QTableWidgetItem(page)
        passwordItem = QTableWidgetItem(pwd)
        passwordItem.setFlags(passwordItem.flags() & ~ Qt.ItemIsEnabled)
        siteItem.setFlags(siteItem.flags() & ~ Qt.ItemIsEditable)
        self._ui.credentials.setItem(row, 0, siteItem)
        self._ui.credentials.setItem(row, 1, passwordItem)

    def delete(self) -> None:
        self._ui.credentials.removeRow(self._selected_row)
        self._file.data.pop(self._selected_item)
        self._ui.passwordEdit.clear()
        self._ui.pageEdit.clear()
        self.toogle_buttons(False, False, False)
        self._file.edited = True

    def update(self) -> None:
        pwd = self._ui.passwordEdit.text()
        self.insert_row(self._selected_row, self._selected_item, pwd)
        self._file.data.update({self._selected_item: pwd})
        self.toogle_buttons(False, False, True)
        self._file.edited = True

    def add(self) -> None:
        pwd = self._ui.passwordEdit.text()
        self._selected_item = self._ui.pageEdit.text()
        self._selected_row = len(self._file.data.keys())
        self._ui.credentials.setRowCount(self._selected_row + 1)
        self.insert_row(self._selected_row, self._selected_item, pwd)
        self._file.data[self._selected_item] = pwd
        self.toogle_buttons(False, False, True)
        self._file.edited = True

    def generate(self) -> None:
        pwd = self._pass.generate()
        self._ui.passwordEdit.setText(pwd)
