import unittest
from cancel_phrase_detector import CancelPhraseDetector
class TestCancelPhraseDetector(unittest.TestCase):
    def test_detect(self):
        detector = CancelPhraseDetector()
        self.assertEqual(detector.detect("audio"), [])
