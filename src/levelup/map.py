from levelup.character import Character
from levelup.position import Position
import random
import array

X_DIMENSION = 10
Y_DIMENSION = 10
class Map:
    startingPosition = None

    def __init__(self):
        random_x = random.randint(0, X_DIMENSION-1)
        random_y = random.randint(0, Y_DIMENSION-1)
        self.startingPosition = Position(random_x, random_y)

    def isPositionValid(self, position):
        return ((0 <= position.x_coordinate) & (position.x_coordinate < X_DIMENSION) & (0 <= position.y_coordinate) & (position.y_coordinate < Y_DIMENSION))

    def getStartingPosition(self):
        return self.startingPosition

    def calculateNewPosition(self, position, direction):
        new_position = Position(position.x_coordinate, position.y_coordinate)
        match direction:
            case 'n':
                new_position.y_coordinate += 1
            case 's':
                new_position.y_coordinate -= 1
            case 'e':
                new_position.x_coordinate += 1
            case 'w':
                new_position.x_coordinate -= 1
            case _:
                pass
        if self.isPositionValid(new_position):
            return new_position
        else:
            return position

class DummyMap(Map):

    def __init(self):
        pass

    def isPositionValid(self, position):
        return True
    
    def getStartingPosition(self):
        return Position(0,0)