import sys
from random import randint

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QPoint

from UI import Ui_MainWindow


class Circles(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.first_paint = False
        self.pushButton.clicked.connect(self.do_paint)

    def paintEvent(self, event):
        if self.first_paint:
            qp = QPainter()
            qp.begin(self)
            self.create_circles(qp)
            qp.end()

    def do_paint(self):
        self.first_paint = True
        self.repaint()

    def create_circles(self, qp):
        n = randint(1, 10)
        for i in range(n):
            r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
            qp.setBrush(QColor(r, g, b))
            d = randint(10, 300)
            r = d // 2
            x, y = randint(d, 800 - d), randint(d, 600 - d)
            qp.drawEllipse(QPoint(x, y), r, r)


def main():
    app = QApplication(sys.argv)
    cs = Circles()
    cs.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
