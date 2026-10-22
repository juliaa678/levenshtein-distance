import unittest

from levenshtein_distance import levenshtein


class TestLevenshtein(unittest.TestCase):
    def test_identical_strings(self):
        self.assertEqual(levenshtein("abc", "abc"), 0)

    def test_one_substitution(self):
        self.assertEqual(levenshtein("cat", "cot"), 1)

    def test_one_insertion(self):
        self.assertEqual(levenshtein("cat", "cats"), 1)

    def test_one_deletion(self):
        self.assertEqual(levenshtein("cats", "cat"), 1)

    def test_completely_different_single_chars(self):
        self.assertEqual(levenshtein("a", "b"), 1)

    def test_two_identical_single_chars(self):
        self.assertEqual(levenshtein("a", "a"), 0)

    def test_empty_first_argument(self):
        self.assertEqual(levenshtein("", "hello"), 5)

    def test_empty_second_argument(self):
        self.assertEqual(levenshtein("hello", ""), 5)

    def test_both_empty(self):
        self.assertEqual(levenshtein("", ""), 0)

    def test_kitten_sitting(self):
        self.assertEqual(levenshtein("kitten", "sitting"), 3)

    def test_flaw_lawn(self):
        self.assertEqual(levenshtein("flaw", "lawn"), 2)

    def test_returns_int_type(self):
        result = levenshtein("abc", "abd")
        self.assertIsInstance(result, int)


if __name__ == "__main__":
    unittest.main()
