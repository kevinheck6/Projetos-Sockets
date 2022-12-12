from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

app = QGuiApplication()

engine = QQmlApplicationEngine()
engine.load("login_qml.qml")

app.exec()
