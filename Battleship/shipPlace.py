from Gameboard import *


def shipPlace(board, r, c, d, ship):
    try:
        # Row is up-down
        # Column is right-left
        row = int(r)
        col = int(c)
        direct = int(d)
    except:
        return False
    else:
        # Direction 1 is down
        # Direction 2 is right
        if direct == 2:
            if col + ship - 1 > 9:
                return False
            else:
                for x in range(ship):
                    if board.getShipLocation(row, col + x) != '0':
                        return False
                for x in range(ship):
                    board.setShip(row, col + x, ship)
                return True
        if direct == 1:
            if row + ship - 1 > 9:
                return False
            else:
                for x in range(ship):
                    if board.getShipLocation(row + x, col) != '0':
                        return False
                for x in range(ship):
                    board.setShip(row + x, col, ship)
                return True
