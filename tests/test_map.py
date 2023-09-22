from unittest import TestCase
from levelup.character import Character
from levelup.position import Position
from levelup.map import Map
from levelup.map import DummyMap

class TestDummyMapInit(TestCase):
    def test_dummy_map_init(self):
        test_map = DummyMap()
        test_position = test_map.getStartingPosition()
        self.assertTrue(test_map.isPositionValid(test_position))

class TestMapInit(TestCase):
    def test_map_init(self):
        test_map = Map()
        test_position = test_map.getStartingPosition()
        print("Test Position is X:" + str(test_position.x_coordinate) + " Y: " + str(test_position.y_coordinate))
        self.assertTrue(test_map.isPositionValid(test_position))

class TestPositionValid(TestCase):
    def test_position_valid(self):
        ARBITRARY_X = 4
        ARBITRARY_Y = 7
        test_map = Map()
        test_position = Position(ARBITRARY_X, ARBITRARY_Y)
        self.assertTrue(test_map.isPositionValid(test_position))

class TestPositionInvalid(TestCase):
    def test_position_invalid(self):
        ARBITRARY_X = 10
        ARBITRARY_Y = 7
        test_map = Map()
        test_position = Position(ARBITRARY_X, ARBITRARY_Y)
        self.assertFalse(test_map.isPositionValid(test_position))