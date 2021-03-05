import unittest

solution = __import__("solution")

class TestSolution(unittest.TestCase):

    # def test_solution(self):
    #     """
    #     different order than my solution
    #     assertItemsEqual unavailable past Py 3.3
    #     """
    #     correct = ["jcatd", "jcate", "jcatf", "kcatd", "kcate", "kcatf", "lcatd", "lcate", "lcatf"]
    #     self.assertItemsEqual(solution.findCombinations("52283","cat"),correct)

    def test_count(self):
        """
        Same number of combinations?
        """
        correct = ["jcatd", "jcate", "jcatf", "kcatd", "kcate", "kcatf", "lcatd", "lcate", "lcatf"]
        self.assertCountEqual(solution.findCombinations('52283','cat'), correct)

    def test_equal(self):
        """
        Test if elements are equal
        """
        correct = ["jcatd", "jcate", "jcatf", "kcatd", "kcate", "kcatf", "lcatd", "lcate", "lcatf"]
        ans = solution.findCombinations('52283', 'cat')
        self.assertEqual(sorted(ans), sorted(correct))

if __name__ == "__main__":
    unittest.main()
