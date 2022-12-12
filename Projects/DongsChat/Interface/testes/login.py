from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication


def callback():
    print('Callback Login')
    print(window.nome_input.text())


app = QApplication()

loader = QUiLoader()
window = loader.load('login.ui')
window.login_button.clicked.connect(callback)

window.show()

app.exec()
