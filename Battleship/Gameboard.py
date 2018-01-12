
class Grid:

    def __init__(self):
        self.grid = []
        self.ship2 = 0
        self.ship3 = 0
        self.ship4 = 0
        self.ship5 = 0
        for x in range(10):
            y = []
            for z in range(10):
                y.append(0)
            self.grid.append(y)

    def getGrid(self):
        return str(self.grid)

    def setShip(self, row, column, shipID):
        self.grid[row][column] = shipID

    def getShipLocation(self, row, column):
        return str(self.grid[row][column])

    def markHit(self, row, column):
        self.grid[row][column] = 8

    def markMiss(self, row, column):
        self.grid[row, column] = 9

    def checkAttack(self, row, column):
        return (str(self.grid[row][column]) != '9' and
                str(self.grid[row][column]) != '8')

    def attack(self, row, column):
        if self.grid[row][column] == 0:
            self.grid[row][column] = 9
            return [False]
        elif self.grid[row][column] == 2:
            self.ship2 += 1
            if self.ship2 == 2:
                self.grid[row][column] = 8
                return (True, self.ship2)
            self.grid[row][column] = 8
            return [True]
        elif self.grid[row][column] == 3:
            self.ship3 += 1
            if self.ship3 == 3:
                self.grid[row][column] = 8
                return (True, self.ship3)
            elif self.ship3 == 6:
                self.grid[row][column] = 8
                return (True, self.ship3 - 2)
            self.grid[row][column] = 8
            return [True]
        elif self.grid[row][column] == 4:
            self.ship4 += 1
            if self.ship4 == 4:
                self.grid[row][column] = 8
                return (True, self.ship4 + 1)
            self.grid[row][column] = 8
            return [True]
        elif self.grid[row][column] == 5:
            self.ship5 += 1
            if self.ship5 == 5:
                self.grid[row][column] = 8
                return (True, self.ship5 + 1)
            self.grid[row][column] = 8
            return [True]

    def __str__(self):
        return str(self.grid)
