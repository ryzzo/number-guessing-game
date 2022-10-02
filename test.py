import unittest
import number_guessing_game as ngg

class TestGameOutput(unittest.TestCase):
    
    def test_output(self):
        program_guess = 500
        
        lower = ngg.compareInput(program_guess, 10)
        self.assertEqual(lower, "smaller")

        larger = ngg.compareInput(program_guess, 600)
        self.assertEqual(larger, "larger")

        correct = ngg.compareInput(program_guess, 500)
        self.assertEqual(correct, "correct")


if __name__ == "__main__":
    unittest.main()