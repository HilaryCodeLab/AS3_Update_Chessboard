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

    def __init__(self, repr=list('HNBQABNH' + 'P' * 8 + '.' * 32 + 'p' * 8 + 'hnbqabnh'),  trait='w'):
        self._repr = repr
        self.trait = trait

    def algebraic_notation(self):
        for y in range(8):
            for x in range(8):
                idx = y * 8 + x
                item = SQUARE_NAMES[idx]
                print(y, x, item)

        board_string = "rnbqkbnrpppppppp................................PPPPPPPPRNBQKBNR"
        square_position = 0
        for a in range(8):
            for b in range(8):
                index = a * 8 + b
                SQUARE_ARRAY[a][b] = [square_position, SQUARE_NAMES[index], board_string[square_position]]
                square_position = square_position + 1
                print(SQUARE_ARRAY[a][b])
            print()

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

    def is_occupied(self, i, j):
        return self._repr[j * 8 + i]

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

    def is_pawn(self):
        # part = "P" if TEAM_WHITES else "p"
        # print(part)
        if TEAM_WHITES:
            file = open('chess_board.txt', mode='r+')
            file.seek(49)
            file.write('.')
            file.seek(41)
            file.write('P')
            file.close()
        else:
            file = open('chess_board.txt', mode='r+')
            file.seek(9)
            file.write('.')
            file.seek(17)
            file.write('p')
            file.close()

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


# if __name__ == '__main__':
    # board = BoardState()
    # board.team()
    # board.pick_team()
    # board.is_same_team(0, 0, -1)
    # board.team_str()
    # board.print_array()
    # board.get_team(5,6)
    # board.is_same_team(0, 0, -1)
    # board.is_pawn()
    # board.moves()
    # board.read_file_to_list()