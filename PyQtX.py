import sys
from os import path

from PyQt5.QtWidgets import QApplication

from mainwindow import MainWindow


def main(argv=None):
    if not argv:
        argv = sys.argv
    
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    return app.exec_()


if __name__ == '__main__':
    sys.exit(main(sys.argv))