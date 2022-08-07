from pathlib import Path
import unittest
import os

import geektrust

class MyMoneyBalalncerTest(unittest.TestCase):
    test_fail_dir: Path = Path(os.getcwd()).joinpath('error_dir')
    test_file_dir: Path = Path(os.getcwd()).joinpath('sample_input')
    def setUp(self) -> None:
        os.makedir(self.test_fail_dir)
        
    def tearDown(self) -> None:
        Path.rmdir(self.test_fail_dir)
        
    def test_main_wrong_dir(self):
        result = os.system(f'python -m geektrust {self.test_fail_dir}')
        self.assertEqual(result, -1)

    def test_full_app(self):
        test_file = self.test_file_dir.joinpath('sample1.txt')
        result = os.system(f'python -m geektrust {test_file}')
        self.assertEqual(result, 0)
        pass
    
if __name__ == '__main__':
    unittest.main()