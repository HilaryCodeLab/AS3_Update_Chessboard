import unittest
from BoardState import BoardState
import main
import os


class MyTestCase(unittest.TestCase):
    def get_file_name(self):
        file_name = 'chess_board.txt'
        main.write_file(file_name)
        return file_name

    def get_file_text(self):
        content = "rnbqkbnrpppppppp................................PPPPPPPPRNBQKBNR"
        return content

    def test_locate_square_index(self):
        result = BoardState()
        x = result.locate_square_index('g2')
        y = (6, 6)
        self.assertEqual(x, y)

    def test_write_file(self):
        self.assertTrue(os.path.isfile(self.get_file_name()))

    def test_read_file(self):
        actual = main.read_file_to_list(main.file_name)
        self.assertEqual(actual, self.get_file_text())


if __name__ == '__main__':
    unittest.main()

suite = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
unittest.TextTestRunner(verbosity=2).run(suite)