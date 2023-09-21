from unittest import TestCase
from levelup.position import Position

class TestPositionInit00(TestCase):
    def test_init(self):
        X_VALUE = 0
        Y_VALUE = 0
        testobj = Position(X_VALUE, Y_VALUE)
        self.assertEqual(X_VALUE, testobj.x_coordinate)
        self.assertEqual(Y_VALUE, testobj.y_coordinate)

class TestPositionInitXY(TestCase):
    def test_init(self):
        X_VALUE = 1
        Y_VALUE = 1
        testobj = Position(X_VALUE, Y_VALUE)
        self.assertEqual(X_VALUE, testobj.x_coordinate)
        self.assertEqual(Y_VALUE, testobj.y_coordinate)