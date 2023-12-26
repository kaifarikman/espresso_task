import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import db


class Application(QMainWindow):
    def __init__(self):
        super().__init__()
        self.start()

    def start(self):
        uic.loadUi('coffee.ui', self)


if __name__ == '__main__':
    db.start_session()
    app = QApplication(sys.argv)
    ex = Application()
    ex.show()
    sys.exit(app.exec_())
