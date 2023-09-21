from levelup.position import Position
from unittest import TestCase
from levelup.character import Character

class TestCharacterInitWithName(TestCase):
    def test_init(self):
        ARBITRARY_NAME = "MyName"
        testobj = Character(ARBITRARY_NAME)
        self.assertEqual(ARBITRARY_NAME, testobj.name)

class TestCharacterInitWithDefaultName(TestCase):
    def test_character_name(self):
        testobj = Character("")
        self.assertEqual("Autobot", testobj.name)


class TestCharacterCurrentPosition(TestCase):
    def test_character_position(self):
        TEST_X=4
        TEST_Y=0
        test_char = Character("")
        test_pos = Position(TEST_X, TEST_Y)
        test_char.changePosition(test_pos)
        self.assertEqual(test_char.currentPosition.x_coordinate,TEST_X)
        self.assertEqual(test_char.currentPosition.y_coordinate,TEST_Y)
