# -*- coding: utf-8 -*-
# Python Minesweeper (pymine)
# Copyright (C) 2014 Andreas Schulz
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA

import sys
from os import path
from PyQt5.QtWidgets import QApplication

from mainwindow import MainWindow

sys.path.insert(0, path.normpath(path.join(path.dirname(path.abspath(__file__)), '..')))


def main(argv=None):
    if not argv:
        argv = sys.argv
    
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    return app.exec_()


if __name__ == '__main__':
    sys.exit(main(sys.argv))
