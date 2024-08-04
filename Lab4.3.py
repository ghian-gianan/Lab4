import unittest
import oxo_dialof_ui

class TestDIalogUI(unittest.TestCase):
    
    def test_startGame(self):
        self.assertEqual(oxo_dialog_ui.startGame(),list(" " * 9)
                         
if __name__ == '__main__':
    unittest.main()