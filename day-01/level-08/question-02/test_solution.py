import unittest
from typing import List

class TestMaxWeightMergedIntervals(unittest.TestCase):
    def test_example1(self):
        intervals = [[1,3,5],[2,6,3],[8,10,2],[15,18,4]]
        expected_max = 8
        expected_merged = [[1,6,8],[8,10,2],[15,18,4]]
        result = max_weight_merged_intervals(intervals)
        self.assertEqual(result, expected_max)
        self.assertEqual(intervals[:len(expected_merged)], expected_merged)

    def test_example2(self):
        intervals = [[1,4,2],[4,5,3]]
        expected_max = 5
        expected_merged = [[1,5,5]]
        result = max_weight_merged_intervals(intervals)
        self.assertEqual(result, expected_max)
        self.assertEqual(intervals[:len(expected_merged)], expected_merged)

    def test_example3(self):
        intervals = [[1,2,1],[3,4,2],[5,6,3]]
        expected_max = 3
        expected_merged = [[1,2,1],[3,4,2],[5,6,3]]
        result = max_weight_merged_intervals(intervals)
        self.assertEqual(result, expected_max)
        self.assertEqual(intervals[:len(expected_merged)], expected_merged)

    def test_single_interval(self):
        intervals = [[5,10,7]]
        expected_max = 7
        expected_merged = [[5,10,7]]
        result = max_weight_merged_intervals(intervals)
        self.assertEqual(result, expected_max)
        self.assertEqual(intervals[:len(expected_merged)], expected_merged)

    def test_all_overlap(self):
        intervals = [[1,5,2],[2,6,3],[3,7,4]]
        expected_max = 9
        expected_merged = [[1,7,9]]
        result = max_weight_merged_intervals(intervals)
        self.assertEqual(result, expected_max)
        self.assertEqual(intervals[:len(expected_merged)], expected_merged)

    def test_no_overlap(self):
        intervals = [[1,2,10],[3,4,20],[5,6,5]]
        expected_max = 20
        expected_merged = [[1,2,10],[3,4,20],[5,6,5]]
        result = max_weight_merged_intervals(intervals)
        self.assertEqual(result, expected_max)
        self.assertEqual(intervals[:len(expected_merged)], expected_merged)

    def test_overlap_at_boundary(self):
        intervals = [[1,3,5],[3,5,2],[5,7,3]]
        expected_max = 10
        expected_merged = [[1,7,10]]
        result = max_weight_merged_intervals(intervals)
        self.assertEqual(result, expected_max)
        self.assertEqual(intervals[:len(expected_merged)], expected_merged)

    def test_large_weights(self):
        intervals = [[1,2,10000],[2,3,10000],[3,4,10000]]
        expected_max = 30000
        expected_merged = [[1,4,30000]]
        result = max_weight_merged_intervals(intervals)
        self.assertEqual(result, expected_max)
        self.assertEqual(intervals[:len(expected_merged)], expected_merged)

if __name__ == '__main__':
    unittest.main()