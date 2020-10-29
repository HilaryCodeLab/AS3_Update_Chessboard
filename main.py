from typing import List
from BoardState import BoardState


file_name ='chess_board.txt'


def write_file(file):
    board_string = "rnbqkbnrpppppppp................................PPPPPPPPRNBQKBNR"
    file = open('chess_board.txt', mode='w')
    x = file.write(board_string)
    file.close()
    # print(len(board_string))


def read_file_to_list(file_name):
    file = open(file_name, mode='r')
    read = file.read()
    file.close()
    return read


def print_board():
    file = open(file_name, mode='r')
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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    write_file(file_name)
    print('Initialize Board')
    read_file_to_list(file_name)
    print_board()
    board = BoardState()
    # test the validation of piece capture from same team
    board.move_piece('a8', 'a7')
    read_file_to_list(file_name)
    print_board()

    # test the move when piece capture from opposite team
    board.move_piece('g2', 'g4')
    read_file_to_list(file_name)
    print_board()
    write_file(file_name)










