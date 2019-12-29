import unittest
from src import program

# this set of tests will aim to test the programs methods, such as its ability to move/evolve cells depending on their
# layout, as well as its ability to generate seeded playing fields.
class TestProgram(unittest.TestCase):

    def test_test(self):
        self.assertEqual(program.calculate_moves([]), True)

    def test_scenario_1(self):
        self.assertEqual(program.calculate_moves([]), True)

    def test_seeded_generation(self):
        test_array = [[False, False, False, False, False], [True, False, False, False, False],
                      [True, True, False, True, True], [False, True, False, False, True],
                      [True, True, False, True, False]]
        self.assertEqual(program.create_seeded_playing_field(5, 5, "hjejs"), test_array)


if __name__ == '__main__':
    unittest.main()
