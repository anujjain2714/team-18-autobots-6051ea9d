from unittest import TestCase
from levelup.position import Position
from levelup.character import Character
from levelup.map import Map
from levelup.map import DummyMap

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

class TestEnterMap(TestCase):
    def test_enter_map(self):
        test_map = DummyMap()
        test_char = Character("")
        test_char.enterMap(test_map)
        self.assertTrue(test_map.isPositionValid(test_char.currentPosition))

class TestEnterMap(TestCase):
    def test_enter_map(self):
        test_map = Map()
        test_char = Character("")
        test_char.enterMap(test_map)
        self.assertTrue(test_map.isPositionValid(test_char.currentPosition))

class TestMoveNorth(TestCase):
    def test_move_north(self):
        test_map = DummyMap()
        test_char = Character("")
        test_char.enterMap(test_map)
        old_move_count = test_char.moveCount
        test_char.move('n')
        self.assertEqual(test_char.currentPosition.y_coordinate,1)
        self.assertEqual(test_char.moveCount, old_move_count+1)