import unittest
from git_diff import *

class TestCalculations(unittest.TestCase):

    def test_longest_common_substring(self):
        self.assertEqual(longest_common_substring("abcde", "ace"), "ace", 'The LCS is wrong.')
        self.assertEqual(longest_common_substring("abcd", "ace"), "ac", 'The LCS is wrong.')
    
    def test_longest_common_subsequence_lines(self):
        lines1 = ["This is a test which contains:", "this is the lcs"]
        lines2 = ["this is the lcs", "we're testing"]
        self.assertEqual(longest_common_substring(lines1, lines2), "this is the lcs", 'The LCSL is wrong.')

        lines1 = ["abc", "xyz"]
        lines2 = ["xyz", "abd", "a"]
        self.assertEqual(longest_common_substring(lines1, lines2), "xyz", 'The LCSL is wrong.')



if __name__ == '__main__':
    unittest.main()