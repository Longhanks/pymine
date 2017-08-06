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

import os
from random import randint

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

from utilities import getResourcesPath
from tile import Tile


class Game(QWidget):
    def __init__(self, rows, columns, mines, parent=None):
        super(Game, self).__init__(parent)
        uic.loadUi(os.path.join(getResourcesPath(),'ui', 'game.ui'), self)
        
        self.btns = []
        self.btnDict = {}

        for column in range(columns):
            for row in range(rows):
                btn = Tile(self)
                self.mainLayout.addWidget(btn, column, row)
                self.btns.append(btn)
                btn.clicked.connect(btn.checkMine)
                btn.rightClicked.connect(btn.setMine)
                btn.myX = column
                btn.myY = row
                btn.setObjectName('btn_' + str(column) + '_' + str(row))
        
        # apply the mines        
        for myInt in self.getListOfInts((len(self.btns) - 1), mines):
            self.btns[myInt].mine = True
            self.btns[myInt].done = True
            
        # add buttons to name-button dictionary
        for btn in self.btns:
            self.btnDict[str(btn.objectName())] = btn
            
        # add all neighbors of all buttons to the buttons
        for btn in self.btns:
            btnTopLeftStr = 'btn_' + str(btn.myX - 1) + '_' + str(btn.myY - 1)
            btnTopStr = 'btn_' + str(btn.myX) + '_' + str(btn.myY - 1)
            btnTopRightStr = 'btn_' + str(btn.myX + 1) + '_' + str(btn.myY - 1)
            btnLeftStr = 'btn_' + str(btn.myX - 1) + '_' + str(btn.myY)
            btnRightStr = 'btn_' + str(btn.myX + 1) + '_' + str(btn.myY)
            btnBottomLeftStr = 'btn_' + str(btn.myX - 1) + '_' + str(btn.myY + 1)
            btnBottomStr = 'btn_' + str(btn.myX) + '_' + str(btn.myY + 1)
            btnBottomRightStr = 'btn_' + str(btn.myX + 1) + '_' + str(btn.myY + 1)
            
            if btnTopLeftStr in self.btnDict:
                btn.neighbors.append(self.btnDict[btnTopLeftStr])
            if btnTopStr in self.btnDict:
                btn.neighbors.append(self.btnDict[btnTopStr])
            if btnTopRightStr in self.btnDict:
                btn.neighbors.append(self.btnDict[btnTopRightStr])
            if btnLeftStr in self.btnDict:
                btn.neighbors.append(self.btnDict[btnLeftStr])
            if btnRightStr in self.btnDict:
                btn.neighbors.append(self.btnDict[btnRightStr])
            if btnBottomLeftStr in self.btnDict:
                btn.neighbors.append(self.btnDict[btnBottomLeftStr])
            if btnBottomStr in self.btnDict:
                btn.neighbors.append(self.btnDict[btnBottomStr])
            if btnBottomRightStr in self.btnDict:
                btn.neighbors.append(self.btnDict[btnBottomRightStr])
                
            for neighbor in btn.neighbors:
                if neighbor.mine:
                    btn.count = btn.count +1
            
            
            
    def getListOfInts(self, numberRange, numberUniques):
        listOfInts = []
        while len(listOfInts) < numberUniques:
            newRand = (randint(0, numberRange))
            if newRand in listOfInts:
                pass
            else:
                listOfInts.append(newRand)
        return listOfInts
                
    def checkIfDone(self):
        for btn in self.btns:
            if btn.done == False:
                return False
        return True
    
    