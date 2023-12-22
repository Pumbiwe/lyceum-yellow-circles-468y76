import random
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class Yellow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)

        self.pushButton = QPushButton(self)

        self.pushButton.clicked.connect(self.drawCircle)
        self.circles = list()

    def paintEvent(self, event):
        painter = QPainter(self)

        for circle in self.circles:
            painter.setPen(QPen(circle[-1], 3, Qt.SolidLine))
            painter.drawEllipse(*circle[:-1], circle[-2])

    def drawCircle(self):
        for i in range(2):
            r = random.randint(0, 100)
            self.circles.append(list([
                random.randint(0, self.width() - r),
                random.randint(0, self.height() - r),
                r,
                random.choice(list([Qt.red, Qt.white, Qt.black, Qt.yellow, Qt.green, Qt.blue]))
            ]))
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Yellow()
    ex.show()
    sys.exit(app.exec())
