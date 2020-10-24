import numpy as np
import chess
import pickle

class Board:

    board = [
        ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],

    ]
    board_string = "rnbqkbnpppppppp...............................PPPPPPPPRNBQKBNR"

    def pickle_object(self):
        # convert object into byte
        file_name = "update_chessboard"
        outfile = open(file_name, "wb")
        pickle.dump(self.board, outfile)
        outfile.close()

    def unpickle_into_object(self):
        # convert data stream into object
        file_name = "update_chessboard"
        infile = open(file_name, 'rb')
        new_list = pickle.load(infile)
        infile.close()
        print(new_list)
        # board_string = ""
        # board_string += "a b c d e f g h\n"
        # print(board_string)
        # for column in new_list:
        #     for item in column:
        #         print(item, end=" ")
        #     print()
        # print("\n" + board_string)

    def update_file(self):
        file_name = 'chess_board.txt'
        f1 = open('chess_board.txt', 'r+')
        # f1.seek(0)
        print(f1.read())
        f1.close()
        # tell() give you current position of item in the file
        # seek() locate the item you looking for by byte,
        # 0 is the beginining of line, 1 is current position, 2 is end of line
        # e.g. seek(12,0) means starting from the beginning of line, count 12 bit ahead to locate the position



