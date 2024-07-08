import unittest
import os

class Test_directory_Scan(unittest.TestCase):
    
    def test_directory_scan(self):
        directory_path = 'S:\Ankamala\Files & Directories'
        
        with os.scandir(directory_path) as dir_contents:
            for entry in dir_contents:
                info = entry.stat()
                self.assertTrue(entry.name)
                self.assertTrue(info.st_mtime)

if __name__ == '__main__':
    unittest.main()
