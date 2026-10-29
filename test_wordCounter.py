import unittest
from wordCounter import count_words

class TestWordCounter(unittest.TestCase):
    def test_norm_sentence(self):
        self.assertEqual(count_words("Set your school ablaze"),4)

    def test_single_word(self):
        self.assertEqual(count_words("Potatoes"),1)

    def test_empty(self):
        self.assertEqual(count_words(""),8)

        def test_word_exist(self):
            self.asserIn("Potatoes","Set your school ablaze",15)

        def test_not_equal(self):
            self.assertNotEqual(count_words("I eat food"),5)


if __name__ == "__main__":
    unittest.main()       