import unittest

class TestMaxWeightTwoNonOverlapping(unittest.TestCase):
    def test_example1(self):
        intervals = [1, 3, 5, 2, 4, 4, 5, 6, 3]
        self.assertEqual(max_weight_two_non_overlapping(intervals), 8)

    def test_example2(self):
        intervals = [1, 5, 10, 2, 3, 5, 4, 6, 8]
        self.assertEqual(max_weight_two_non_overlapping(intervals), 13)

    def test_example3(self):
        intervals = [1, 2, 5, 2, 3, 6]
        self.assertEqual(max_weight_two_non_overlapping(intervals), 0)

    def test_all_overlap(self):
        # All intervals overlap, no valid pair
        intervals = [1, 10, 5, 2, 9, 6, 3, 8, 7]
        self.assertEqual(max_weight_two_non_overlapping(intervals), 0)

    def test_disjoint_intervals(self):
        # Intervals are completely separate
        intervals = [1, 2, 10, 3, 4, 20, 5, 6, 30]
        # Best pair: 20+30=50 (intervals 2 and 3) or 10+30=40, etc.
        self.assertEqual(max_weight_two_non_overlapping(intervals), 50)

    def test_large_weights(self):
        intervals = [1, 2, 1000000000, 3, 4, 1000000000]
        self.assertEqual(max_weight_two_non_overlapping(intervals), 2000000000)

    def test_unsorted_input(self):
        # Input not sorted by start
        intervals = [5, 6, 3, 1, 3, 5, 2, 4, 4]
        self.assertEqual(max_weight_two_non_overlapping(intervals), 8)

    def test_multiple_valid_pairs(self):
        intervals = [1, 2, 10, 2, 3, 5, 3, 4, 8, 4, 5, 7]
        # Valid pairs: (10,8)=18, (10,7)=17, (5,7)=12, (5,8)=13, etc.
        # Best is 10+8=18 (intervals [1,2,10] and [3,4,8])
        self.assertEqual(max_weight_two_non_overlapping(intervals), 18)

if __name__ == '__main__':
    unittest.main()
