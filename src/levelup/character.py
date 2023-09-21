from levelup.position import Position
class Character:
    name = "Autobot"
    currentPosition = None

    def __init__(self, character_name):
        if character_name != "":
            self.name = character_name

    def changePosition(self, new_position):
        self.currentPosition = new_position

