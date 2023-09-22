from levelup.position import Position
class Character:
    name = "Autobot"
    currentPosition = None
    currentMap = None
    moveCount = 0

    def __init__(self, character_name):
        if character_name != "":
            self.name = character_name

    def changePosition(self, new_position):
        self.currentPosition = new_position
    
    def enterMap(self, map):
        starting_position = map.getStartingPosition()
        self.changePosition(starting_position)
        self.currentMap = map

    def move(self, direction):
        new_position = self.currentMap.calculateNewPosition(self.currentPosition, direction)
        self.changePosition(new_position)
        self.moveCount += 1

