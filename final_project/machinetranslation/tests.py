import unittest
from translator import englishToFrench, frenchToEnglish

class TestTranslator(unittest.TestCase):
    def test_englishToFrench(self):
        if englishText = '':
            print('No entry to translate')
        else:
            self.assertEqual(englishToFrench('Hello'),'Bonjour')

    def test_frenchToEnglish(self):
        if frenchText = '':
            print('No entry to translate')
        else:
            self.assertEqual(frenchToEnglish('Bonjour'),'Hello')
