import random
import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QApplication, QMainWindow


class Yellow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.drawCircle)
        self.circles = list()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.yellow, 3, Qt.SolidLine))

        for circle in self.circles:
            painter.drawEllipse(*circle, circle[-1])

    def drawCircle(self):
        for i in range(2):
            r = random.randint(0, 100)
            self.circles.append(list([
                random.randint(0, self.width() - r),
                random.randint(0, self.height() - r),
                r
            ]))
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Yellow()
    ex.show()
    sys.exit(app.exec())
