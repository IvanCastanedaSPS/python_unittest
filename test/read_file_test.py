import unittest
from helpers.manage_txt_files import read_file

class probar_funciones(unittest.TestCase):
    def test_file(self):
        file_path = 'file2.txt'
        read_file(file_path)

if __name__ == "__main__":
    unittest.main()