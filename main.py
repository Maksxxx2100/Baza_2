import sqlalchemy as db
import sqlite3

import sys
from PyQt5.QtWidgets import QApplication

from windows import FilmList

sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook


app = QApplication(sys.argv)
ex = FilmList()
ex.show()
sys.exit(app.exec_())