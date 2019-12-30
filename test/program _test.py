import unittest
from src import program


# this set of tests will aim to test the programs methods, such as its ability to move/evolve cells depending on their
# layout, as well as its ability to generate seeded playing fields.
class TestProgram(unittest.TestCase):

    def test_scenario_0_no_interactions(self):
        input_array = [[False, False, False],
                       [False, False, False],
                       [False, False, False]]

        output_array = [[False, False, False],
                        [False, False, False],
                        [False, False, False]]

        self.assertEqual(program.calculate_moves(input_array), output_array)

    def test_scenario_1_underpopulation(self):
        input_array = [[False, False, False],
                       [False, True, False],
                       [False, True, False]]

        output_array = [[False, False, False],
                        [False, False, False],
                        [False, False, False]]

        self.assertEqual(program.calculate_moves(input_array), output_array)

    def test_scenario_2_overcrowding(self):
        input_array = [[False, True, True],
                       [False, True, True],
                       [False, True, True]]

        output_array = [[False, True, True],
                        [True, False, False],
                        [False, True, True]]

        self.assertEqual(program.calculate_moves(input_array), output_array)

    def test_scenario_3_survival(self):
        input_array = [[False, False, False],
                       [False, True, True],
                       [False, True, True]]

        output_array = [[False, False, False],
                        [False, True, True],
                        [False, True, True]]

        self.assertEqual(program.calculate_moves(input_array), output_array)

    def test_scenario_4_creation_of_life(self):
        input_array = [[False, False, False],
                       [False, False, True],
                       [False, True, True]]

        output_array = [[False, False, False],
                        [False, True, True],
                        [False, True, True]]

        self.assertEqual(program.calculate_moves(input_array), output_array)

    def test_scenario_6_expected_game_outcome_for_seeded_grid(self):
        input_array = [[False, True, False],
                       [False, True, False],
                       [False, True, False]]

        output_array = [[False, False, False],
                        [True, True, True],
                        [False, False, False]]

        self.assertEqual(program.calculate_moves(input_array), output_array)
        self.assertEqual(program.calculate_moves(output_array), input_array)

    def test_seeded_generation(self):
        test_array = [[False, False, False, False, False],
                      [True, False, False, False, False],
                      [True, True, False, True, True],
                      [False, True, False, False, True],
                      [True, True, False, True, False]]
        self.assertEqual(program.create_seeded_playing_field(5, 5, "hjejs"), test_array)


if __name__ == '__main__':
    unittest.main()
