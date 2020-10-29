from typing import List

TEAM_WHITES = 1
TEAM_BLACKS = -1
FILE_NAMES = ["a", "b", "c", "d", "e", "f", "g", "h"]
RANK_NAMES = ["1", "2", "3", "4", "5", "6", "7", "8"]
SQUARE_NAMES = [f + r for r in RANK_NAMES[::-1] for f in FILE_NAMES]
YOUR_FILE ='chess_board.txt'
SQUARE_ARRAY = [list([None] * 8) for _ in range(8)]


class BoardState:

    def __init__(self, trait='w'):
        self.trait = trait
        self.square_array = [list([None] * 8) for _ in range(8)]

        # loop through list of RANK_NAMES and SQUARE_NAMES
        for y in range(8):
            for x in range(8):
                idx = y * 8 + x
                item = SQUARE_NAMES[idx]
                # print(y, x, item)

        board_string = "rnbqkbnrpppppppp................................PPPPPPPPRNBQKBNR"
        square_position = 0

        # put algebraic notations of chess pieces into 8 x 8 list
        for a in range(8):
            for b in range(8):
                index = a * 8 + b
                SQUARE_ARRAY[a][b] = [square_position, SQUARE_NAMES[index], board_string[square_position]]
                square_position = square_position + 1
            #     print(SQUARE_ARRAY[a][b])
            # print()

    def print_board(self):
        file = open(YOUR_FILE, mode='r')
        board = file.read()
        file.close()
        my_list_of_lists: List[List[None]] = [list([None] * 8) for _ in range(8)]
        for x in range(8):
            for y in range(8):
                idx = x * 8 + y
                my_list_of_lists[x][y] = board[idx]
        # print(my_list_of_lists)

        # print board in grid table
        board_string = ""
        board_string += "a b c d e f g h\n"
        print(board_string)
        for column in my_list_of_lists:
            for item in column:
                print(item, end=" ")
            print()
        print("\n" + board_string)

    # get the index of squares from 2d array
    def locate_square_index(self, square_position):
        for a in range(8):
            for b in range(8):
                if SQUARE_ARRAY[a][b][1] == square_position:
                    return a, b

    def move_piece(self, move_from, move_to):
        piece_from = self.locate_square_index(move_from)
        piece_to = self.locate_square_index(move_to)
        piece = SQUARE_ARRAY[piece_from[0]][piece_from[1]][2]
        go_to = SQUARE_ARRAY[piece_to[0]][piece_to[1]][2]
        file = open(YOUR_FILE, mode='r+')

        # validate if the move is made on the same side for white
        if piece.isupper():
            if not go_to.isupper():
                # locate the piece from a position
                file.seek(SQUARE_ARRAY[piece_from[0]][piece_from[1]][0])
                file.write(".")

                # locate the go-to position
                file.seek(SQUARE_ARRAY[piece_to[0]][piece_to[1]][0])
                file.write(piece)
                file.close()
            else:
                print("invalid move, same team cannot capture it own kind!")
        else:
            # validate if the move is made on the same side for black
            if piece != piece.isupper():
                if not go_to.islower():
                    file.seek(SQUARE_ARRAY[piece_from[0]][piece_from[1]][0])
                    file.write(".")
                    file.seek(SQUARE_ARRAY[piece_to[0]][piece_to[1]][0])
                    file.write(piece)
                    file.close()
                else:
                    print("invalid move, same team cannot capture it own kind!")

    def user_input(self):
        move_from = input("move from: ")
        move_to = input("move to: ")
        piece_from = self.locate_square_index(move_from)
        piece = SQUARE_ARRAY[piece_from[0]][piece_from[1]][2]
        if piece.isupper():
            self.move_piece(move_from, move_to)
            self.print_board()
            self.user_input()
        else:
            print("White has to go first")
        while piece.islower():
            self.move_piece(move_from, move_to)
            self.print_board()
            break



