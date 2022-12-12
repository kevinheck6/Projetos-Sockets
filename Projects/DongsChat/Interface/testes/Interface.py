from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QAction
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QVBoxLayout, QMainWindow
from qdarktheme import load_stylesheet


def callback():
    print('Button was clicked')



class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        base = QWidget()
        layout = QVBoxLayout()

        font = QFont()
        font.setPixelSize(90)
        base.setFont(font)

        self.label = QLabel("Testing")
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        button = QPushButton("Button")
        button.setFont(font)

        button.clicked.connect(self.muda_label)

        layout.addWidget(self.label)
        layout.addWidget(button)

        base.setLayout(layout)
        self.setCentralWidget(base)

        menu = self.menuBar()
        arquivo_menu = menu.addMenu("Arquivo")
        action = QAction("Print")
        action.triggered.connect(callback)
        arquivo_menu.addAction(action)

    def muda_label(self):
        self.label.setText('Clicked')


app = QApplication()
app.setStyleSheet(load_stylesheet())

window = Window()
window.show()

app.exec()
