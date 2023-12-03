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
        self.button.clicked.connect(self.draw)

    def draw(self):
        canvas = QPixmap(self.background.size())
        self.qp = QPainter(canvas)
        pen = QPen()
        pen.setWidth(2)
        pen.setColor(QColor(255, 142, 0))
        self.qp.setPen(pen)
        self.qp.drawEllipse(random.randint(0, 450), random.randint(0, 450),
                            random.randint(0, 450), random.randint(0, 450))
        self.qp.end()
        self.background.setPixmap(canvas)