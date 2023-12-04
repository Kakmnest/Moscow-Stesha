import sys
import random
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Drawer(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.setWindowTitle('Думали, что это розовые параболы? А это желтые окружности')
        self.do_paint = False
        self.canvas = QPixmap(self.label.size())
        qp = QPainter(self.canvas)
        qp.setBrush(QColor(255, 255, 255))
        qp.drawRect(0, 0, 500, 500)
        qp.end()
        self.pushButton.clicked.connect(self.draw)


    def draw(self):
        self.qp = QPainter(self.canvas)
        pen = QPen()
        pen.setWidth(2)
        pen.setColor(QColor(255, 142, 0))
        self.qp.setPen(pen)
        self.qp.setBrush(QColor(240, 180, 0))
        x = random.randint(0, 400)
        y = random.randint(0, 400)
        d = random.randint(20, 300)
        self.qp.drawEllipse(x, y, d, d)
        self.qp.end()
        self.label.setPixmap(self.canvas)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Drawer()
    ex.show()
    sys.exit(app.exec_())