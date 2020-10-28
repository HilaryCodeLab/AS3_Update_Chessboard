from typing import List

TEAM_WHITES = 1
TEAM_BLACKS = -1
FILE_NAMES = ["a", "b", "c", "d", "e", "f", "g", "h"]
RANK_NAMES = ["1", "2", "3", "4", "5", "6", "7", "8"]
SQUARE_NAMES = [f + r for r in RANK_NAMES[::-1] for f in FILE_NAMES]
RES = SQUARE_NAMES[::-1]
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
        file = open(YOUR_FILE, mode='r+')

        # locate the piece from a position
        file.seek(SQUARE_ARRAY[piece_from[0]][piece_from[1]][0])
        file.write(".")

        # locate the go-to position
        file.seek(SQUARE_ARRAY[piece_to[0]][piece_to[1]][0])
        file.write(piece)
        file.close()

    def team(self):
        return print(TEAM_WHITES) if self.trait == 'w' else TEAM_BLACKS

    def pick_team(self):
        user_input = input("pick a team: Black or White: ")
        if user_input == "white," or "w":
            print("you are on white team")
            return TEAM_WHITES
        else:
            print("you are on black team")
            return TEAM_BLACKS

    def team_str(team):
        # return 'black' if team == TEAM_BLACKS else 'white'
        if team == TEAM_BLACKS:
            print('black')
        else:
            print('white')

    def get_team(self, i, j):
        p = self._repr[j * 8 + i]
        if p == '.':
            return 0
        elif p in 'PRHNBQAZ':
            return TEAM_WHITES
        else:
            return TEAM_BLACKS


    def is_same_team(self, i, j, team):
        possibleparts = 'PRHNBQAZ' if team == TEAM_WHITES else 'prhnbqaz'
        return self._repr[j * 8 + i] in possibleparts


    def moves(self):
        move_input = input("place your move: ")
        if move_input == 'P':
            self.is_pawn()

    def read_file_to_list(self):
        file = open('chess_board.txt', mode='r')
        board = file.read()
        file.close()
        my_list_of_lists: List[List[None]] = [list([None] * 8) for _ in range(8)]
        for x in range(8):
            for y in range(8):
                idx = x * 8 + y
                my_list_of_lists[x][y] = board[idx]
        print(my_list_of_lists)

        # print board in grid table
        board_string = ""
        board_string += "a b c d e f g h\n"
        print(board_string)
        for column in my_list_of_lists:
            for item in column:
                print(item, end=" ")
            print()
        print("\n" + board_string)


