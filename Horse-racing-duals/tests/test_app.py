import unittest
from src import app


class TestApp(unittest.TestCase):
    def test_difference_between_6_and_2_is_4(self):
        self.assertEquals(4, app.calculate_difference(6, 2), '|6-2| should be 4')

    def test_difference_between_2_and_6_is_4(self):
        self.assertEquals(4, app.calculate_difference(2, 6), '|2-6| should be 4')

    def test_calculate_closest_difference_with_sorted_elements(self):
        candidates = [5, 8, 12, 36, 80]
        self.assertEquals(3, app.calculate_closest_difference_with_sorted_elements(candidates, 5))


if __name__ == '__main__':
    unittest.main()
