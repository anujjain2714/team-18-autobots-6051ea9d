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

class TestCalculateNewPositionNorth(TestCase):
    def test_calc_new_position_north(self):
        #Assumption: this is in the centre of map, not near a boundary
        ARBITRARY_X = 5
        ARBITRARY_Y = 5
        test_map = Map()
        test_position = Position(ARBITRARY_X, ARBITRARY_Y)
        test_new_position = test_map.calculateNewPosition(test_position, 'n')
        print("Test Position is X:" + str(test_position.x_coordinate) + " Y: " + str(test_position.y_coordinate))
        print("New Position is X:" + str(test_new_position.x_coordinate) + " Y: " + str(test_new_position.y_coordinate))
        self.assertEqual(test_position.y_coordinate+1, test_new_position.y_coordinate)
        
class TestCalculateNewPositionSouth(TestCase):
    def test_calc_new_position_south(self):
        #Assumption: this is in the centre of map, not near a boundary
        ARBITRARY_X = 5
        ARBITRARY_Y = 5
        test_map = Map()
        test_position = Position(ARBITRARY_X, ARBITRARY_Y)
        test_new_position = test_map.calculateNewPosition(test_position, 's')
        print("Test Position is X:" + str(test_position.x_coordinate) + " Y: " + str(test_position.y_coordinate))
        print("New Position is X:" + str(test_new_position.x_coordinate) + " Y: " + str(test_new_position.y_coordinate))
        self.assertEqual(test_position.y_coordinate-1, test_new_position.y_coordinate)

class TestCalculateNewPositionEast(TestCase):
    def test_calc_new_position_east(self):
        #Assumption: this is in the centre of map, not near a boundary
        ARBITRARY_X = 5
        ARBITRARY_Y = 5
        test_map = Map()
        test_position = Position(ARBITRARY_X, ARBITRARY_Y)
        test_new_position = test_map.calculateNewPosition(test_position, 'e')
        print("Test Position is X:" + str(test_position.x_coordinate) + " Y: " + str(test_position.y_coordinate))
        print("New Position is X:" + str(test_new_position.x_coordinate) + " Y: " + str(test_new_position.y_coordinate))
        self.assertEqual(test_position.x_coordinate+1, test_new_position.x_coordinate)

class TestCalculateNewPositionWest(TestCase):
    def test_calc_new_position_west(self):
        #Assumption: this is in the centre of map, not near a boundary
        ARBITRARY_X = 5
        ARBITRARY_Y = 5
        test_map = Map()
        test_position = Position(ARBITRARY_X, ARBITRARY_Y)
        test_new_position = test_map.calculateNewPosition(test_position, 'w')
        print("Test Position is X:" + str(test_position.x_coordinate) + " Y: " + str(test_position.y_coordinate))
        print("New Position is X:" + str(test_new_position.x_coordinate) + " Y: " + str(test_new_position.y_coordinate))
        self.assertEqual(test_position.x_coordinate-1, test_new_position.x_coordinate)

class TestCalculateNewPositionNorthBoundary(TestCase):
    def test_calc_new_position_north_boundary(self):
        #Assumption: this is at north boundary of map
        ARBITRARY_X = 2
        ARBITRARY_Y = 9
        test_map = Map()
        test_position = Position(ARBITRARY_X, ARBITRARY_Y)
        test_new_position = test_map.calculateNewPosition(test_position, 'n')
        print("Test Position is X:" + str(test_position.x_coordinate) + " Y: " + str(test_position.y_coordinate))
        print("New Position is X:" + str(test_new_position.x_coordinate) + " Y: " + str(test_new_position.y_coordinate))
        self.assertEqual(test_position.y_coordinate, test_new_position.y_coordinate)

class TestCalculateNewPositionSouthBoundary(TestCase):
    def test_calc_new_position_south_boundary(self):
        #Assumption: this is at south boundary of map
        ARBITRARY_X = 2
        ARBITRARY_Y = 0
        test_map = Map()
        test_position = Position(ARBITRARY_X, ARBITRARY_Y)
        test_new_position = test_map.calculateNewPosition(test_position, 's')
        print("Test Position is X:" + str(test_position.x_coordinate) + " Y: " + str(test_position.y_coordinate))
        print("New Position is X:" + str(test_new_position.x_coordinate) + " Y: " + str(test_new_position.y_coordinate))
        self.assertEqual(test_position.y_coordinate, test_new_position.y_coordinate)

class TestCalculateNewPositionEastBoundary(TestCase):
    def test_calc_new_position_east_boundary(self):
        #Assumption: this is at east boundary of map
        ARBITRARY_X = 9
        ARBITRARY_Y = 7
        test_map = Map()
        test_position = Position(ARBITRARY_X, ARBITRARY_Y)
        test_new_position = test_map.calculateNewPosition(test_position, 'e')
        print("Test Position is X:" + str(test_position.x_coordinate) + " Y: " + str(test_position.y_coordinate))
        print("New Position is X:" + str(test_new_position.x_coordinate) + " Y: " + str(test_new_position.y_coordinate))
        self.assertEqual(test_position.x_coordinate, test_new_position.x_coordinate)

class TestCalculateNewPositionWestBoundary(TestCase):
    def test_calc_new_position_west_boundary(self):
        #Assumption: this is at west boundary of map
        ARBITRARY_X = 0
        ARBITRARY_Y = 6
        test_map = Map()
        test_position = Position(ARBITRARY_X, ARBITRARY_Y)
        test_new_position = test_map.calculateNewPosition(test_position, 'w')
        print("Test Position is X:" + str(test_position.x_coordinate) + " Y: " + str(test_position.y_coordinate))
        print("New Position is X:" + str(test_new_position.x_coordinate) + " Y: " + str(test_new_position.y_coordinate))
        self.assertEqual(test_position.x_coordinate, test_new_position.x_coordinate)

class TestGetTotalPositions(TestCase):
    def test_get_total_positions(self):
        test_map = Map()
        self.assertEqual(test_map.getTotalPositions(),100)
