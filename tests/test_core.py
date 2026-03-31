import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))

from sable_operator import top_terms, word_counts


class WordCountsTests(unittest.TestCase):
    def test_word_counts_normalizes_and_counts(self) -> None:
        text = "Hello, hello... HELLO? world!"
        self.assertEqual(word_counts(text), {"hello": 3, "world": 1})

    def test_word_counts_handles_empty(self) -> None:
        self.assertEqual(word_counts("---"), {})

    def test_top_terms_sorting_and_limit(self) -> None:
        text = "b b a c c c a"
        self.assertEqual(top_terms(text, limit=2), [("c", 3), ("a", 2)])

    def test_top_terms_non_positive_limit(self) -> None:
        self.assertEqual(top_terms("a a b", limit=0), [])


if __name__ == "__main__":
    unittest.main()
