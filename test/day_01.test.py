
import unittest
from src.day_01 import SpecialDial


class TestDay1(unittest.TestCase):

    def setUp(self):
        self.dial = SpecialDial()

    #TESTING ENDING UP IN ZERO
    def test_it_should_give_1_from_0_to_0_RIGHT(self):
        #Right
        self.dial.pointer = 0
        movement = [('R',100)]
        self.dial.move_dial(movement)
        self.assertEqual(self.dial.zeros, 1)  # Assert expected outcome

    def test_it_should_give_1_from_0_to_0_LEFT(self):
        self.dial.pointer = 0
        movement = [('L', 100)]
        self.dial.move_dial(movement)
        self.assertEqual(self.dial.zeros, 1)  # Assert expected outcome

    def test_it_should_give_1_from_N_to_0_RIGHT(self):
        self.dial.pointer = 5
        movement = [('R', 95)]
        self.dial.move_dial(movement)
        self.assertEqual(self.dial.zeros, 1)  # Assert expected outcome
    def test_it_should_give_1_from_N_to_0_LEFT(self):
        self.dial.pointer = 5
        movement = [('L', 5)]
        self.dial.move_dial(movement)
        self.assertEqual(self.dial.zeros, 1)  # Assert expected outcome

    # TESTING NOT PASSING BY ZERO
    def test_it_should_give_0_from_0_to_N_RIGHT(self):
        self.dial.pointer = 0
        movement = [('R',50)]
        self.dial.move_dial(movement)
        self.assertEqual(self.dial.zeros, 0)  # Assert


    def test_it_should_give_0_from_0_to_N_LEFT(self):
        self.dial.pointer = 0
        movement = [('L',50)]
        self.dial.move_dial(movement)
        self.assertEqual(self.dial.zeros, 0)  # Assert

    def test_it_should_give_0_from_N_to_N_RIGHT(self):
        self.dial.pointer = 5
        movement = [('R',5)]
        self.dial.move_dial(movement)
        self.assertEqual(self.dial.zeros, 0)  # Assert

    def test_it_should_give_0_from_N_to_N_LEFT(self):
        self.dial.pointer = 50
        movement = [('L',5)]
        self.dial.move_dial(movement)
        self.assertEqual(self.dial.zeros, 0)  # Assert


    # PASSES BY  ZERO FROM ZERO/FROM N TO ZERO/TO N( LEFT)
    def test_it_should_give_1_from_0_to_N_LEFT(self):
        self.dial.pointer = 0
        movement = [('L',101)]
        self.dial.move_dial(movement)
        self.assertEqual(self.dial.zeros, 1)  # Assert

    def test_it_should_give_2_from_0_to_0_LEFT(self):
        self.dial.pointer = 0
        movement = [('L',200)]
        self.dial.move_dial(movement)
        self.assertEqual(self.dial.zeros, 2)  # Assert

    def test_it_should_give_2_from_N_to_N_LEFT(self):
        self.dial.pointer = 5
        movement = [('L',200)]
        self.dial.move_dial(movement)
        self.assertEqual(self.dial.zeros, 2)  # Assert

    # EDGE CASES FOR RIGHT MOVEMENT
    def test_it_should_give_1_from_0_to_N_RIGHT(self):
        """Moving right from 0 by 101 should pass 0 once (at position 100)"""
        self.dial.pointer = 0
        movement = [('R', 101)]
        self.dial.move_dial(movement)
        self.assertEqual(self.dial.zeros, 1)  # Assert

    def test_it_should_give_2_from_0_to_0_RIGHT(self):
        """Moving right from 0 by 200 should pass 0 twice"""
        self.dial.pointer = 0
        movement = [('R', 200)]
        self.dial.move_dial(movement)
        self.assertEqual(self.dial.zeros, 2)  # Assert

    def test_it_should_give_2_from_N_to_N_RIGHT(self):
        """Moving right from 5 by 200 should pass 0 twice"""
        self.dial.pointer = 5
        movement = [('R', 200)]
        self.dial.move_dial(movement)
        self.assertEqual(self.dial.zeros, 2)  # Assert

    def test_it_should_give_1_from_N_to_N_RIGHT_crosses_once(self):
        """Moving right from 99 by 1 should pass 0 once"""
        self.dial.pointer = 99
        movement = [('R', 1)]
        self.dial.move_dial(movement)
        self.assertEqual(self.dial.zeros, 1)  # Assert

    def test_it_should_give_3_from_50_RIGHT_multiple_rotations(self):
        """Moving right from 50 by 250 should pass 0 three times (at 50, 150, 250 moves)"""
        self.dial.pointer = 50
        movement = [('R', 250)]
        self.dial.move_dial(movement)
        self.assertEqual(self.dial.zeros, 3)  # Assert

    # EDGE CASES FOR EXACT BOUNDARIES
    def test_it_should_give_0_from_99_LEFT_by_99(self):
        """Moving left from 99 by 99 lands on 0, should count as 1"""
        self.dial.pointer = 99
        movement = [('L', 99)]
        self.dial.move_dial(movement)
        self.assertEqual(self.dial.zeros, 1)  # Assert

    def test_it_should_give_0_from_1_RIGHT_by_99(self):
        """Moving right from 1 by 99 lands on 0 (wraps), should count as 1"""
        self.dial.pointer = 1
        movement = [('R', 99)]
        self.dial.move_dial(movement)
        self.assertEqual(self.dial.zeros, 1)  # Assert


if __name__ == '__main__':
    unittest.main()