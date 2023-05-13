import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        self.assertIsNone(english_to_french(''),msg='No input')

    def test_french_to_english(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        self.assertIsNone(french_to_english(''),msg='no input')
        self.assertIsNot('')

if __name__ == "__main__":
    unnittest.main()