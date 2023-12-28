import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import db


class Application(QMainWindow):
    def __init__(self):
        super().__init__()
        self.start()

    def start(self):
        uic.loadUi('main.ui', self)
        self.button.clicked.connect(self.get_coffee)

    def get_coffee(self):
        coffee = self.finder.text()
        info = db.get_coffee_by_name(coffee)
        if info is None:
            self.error.setText("Такое кофе по названию не найдено")
            info = ("", "", "", "", "", "", "")
        self.ID.setText(f"ID {info[0]}")
        self.name.setText(f"Название: {info[1]}")
        self.roasting.setText(f"Степень обжарки: {info[2]}")
        self.ground.setText(f"тип обжарки: {info[3]}")
        self.about.setText(f"Описание вкуса: {info[4]}")
        self.price.setText(f"Цена: {info[5]}")
        self.volume.setText(f"Объём: {info[6]}")


if __name__ == '__main__':
    db.start_session()
    app = QApplication(sys.argv)
    ex = Application()
    ex.show()
    sys.exit(app.exec_())
