import unittest
from git_diff import longest_common_substring

class TestCalculations(unittest.TestCase):

    def test_longest_common_substring(self):
        self.assertEqual(longest_common_substring("abcde", "ace"), "ace", 'The LCSs is wrong.')
        self.assertEqual(longest_common_substring("abcd", "ace"), "ac", 'The LCSs is wrong.')



if __name__ == '__main__':
    unittest.main()