import unittest
from src.metrics import Precision

class Test_Metrics(unittest.TestCase):
    def test_precision(self):
        y_true = [0,0]
        y_pred = [0,0]

        result = Precision(y_true, y_pred)

        self.assertEqual(result, 100)

if __name__ == '__main__':
    unittest.main()
        