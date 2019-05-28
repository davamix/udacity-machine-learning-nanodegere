import unittest
import src.metrics as m

class Test_Metrics(unittest.TestCase):
    def test_precision(self):
        y_true = [0,0]
        y_pred = [0,0]
        
        result = m.Precision(y_true, y_pred)

        self.assertEqual(result, 0)
    
    def test_recall(self):
        y_true = [0,0]
        y_pred = [0,0]
        
        result = m.Recall(y_true, y_pred)
        
        self.assertEqual(result, 100)

if __name__ == 'tests.metrics.test_metrics':
    unittest.main()
        