#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 11:29:28 2017

@author: snehanagaraj
"""


class Board(object):

    def __init__(self, input_string):
        self.input_board = input_string
        self.letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        self.populate_board()

    def populate_board(self):
        self.variablesDomainDict = {}
        parts = []
        for i in range(0, len(self.input_board), 9):
            parts.append(self.input_board[i:i + 9])
        for i in range(9):
            for j in range(9):
                self.variablesDomainDict[
                    self.letters[i] + str(j + 1)] = set([parts[i][j]])
        self.setDomainForVariables()

    def setDomainForVariables(self):
        for key, value in self.variablesDomainDict.items():
            if(value == {'0'}):
                self.variablesDomainDict[key] = set(
                    ['1', '2', '3', '4', '5', '6', '7', '8', '9'])
                neighbours = self.getNeighbours(key)
                for neighbour in neighbours:
                    if(len(self.variablesDomainDict[neighbour]) == 1):
                        self.variablesDomainDict[key] = \
                            self.variablesDomainDict[
                                key] - self.variablesDomainDict[neighbour]
        self.buildConstraintsForVariables()

    def cubeConstraints(self, i, j):
        cubeList = []
        for row in range(i, i + 3):
            for col in range(j, j + 3):
                cubeList.append(self.letters[row] + str(col + 1))
        for var1 in cubeList:
            for var2 in cubeList:
                if((var1[0] != var2[0] and var1[1] != var2[1])):
                    if ((var1, var2) not in self.constraints):
                        self.constraints.add((var1, var2))

    def buildConstraintsForVariables(self):
        self.constraints = set()
        # row and column constraints
        for var1 in self.variablesDomainDict.keys():
            for var2 in self.variablesDomainDict.keys():
                if((var1[0] == var2[0] and var1[1] != var2[1]) or
                        (var1[0] != var2[0] and var1[1] == var2[1])):
                    if((var1, var2) not in self.constraints):
                        self.constraints.add((var1, var2))
        # cube constraints
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                self.cubeConstraints(i, j)

    def getNeighbours(self, variable):
        neighbours = []
        # row neighbours
        for i in range(1, 10):
            if((variable[0] + str(i)) != variable):
                neighbours.append(variable[0] + str(i))
        # column neighbours
        for i in range(9):
            if((self.letters[i] + str(variable[1])) != variable):
                neighbours.append(self.letters[i] + str(variable[1]))
        # cube neighbours
        letterIndex = self.letters.index(variable[0])
        row = int(int(letterIndex / 3) * 3)
        col = int(int((int(variable[1]) - 1) / 3) * 3)
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                if(self.letters[i] + str(j + 1) != variable and
                        self.letters[i] + str(j + 1) not in neighbours):
                    neighbours.append(self.letters[i] + str(j + 1))
        return neighbours
