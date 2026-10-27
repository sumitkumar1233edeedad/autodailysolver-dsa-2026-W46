import unittest

class TestTopKFrequent(unittest.TestCase):
    def test_example1(self):
        nums = [1,1,1,2,2,3]
        k = 2
        result = topKFrequent(nums, k)
        self.assertEqual(set(result), {1, 2})
        self.assertEqual(len(result), k)
    
    def test_example2(self):
        nums = [1]
        k = 1
        result = topKFrequent(nums, k)
        self.assertEqual(result, [1])
    
    def test_example3(self):
        nums = [4,1,-1,2,-1,2,3]
        k = 2
        result = topKFrequent(nums, k)
        self.assertEqual(set(result), {-1, 2})
        self.assertEqual(len(result), k)
    
    def test_all_same(self):
        nums = [5,5,5,5]
        k = 1
        result = topKFrequent(nums, k)
        self.assertEqual(result, [5])
    
    def test_k_equals_unique(self):
        nums = [1,2,3,4]
        k = 4
        result = topKFrequent(nums, k)
        self.assertEqual(set(result), {1,2,3,4})
        self.assertEqual(len(result), k)
    
    def test_negative_numbers(self):
        nums = [-1,-1,-2,-2,-3]
        k = 2
        result = topKFrequent(nums, k)
        self.assertEqual(set(result), {-1, -2})
        self.assertEqual(len(result), k)

if __name__ == '__main__':
    unittest.main()
