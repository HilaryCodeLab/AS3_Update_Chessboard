from typing import List

from board import Board


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def print_string():
    brdStr = ""
    # brdStr += " . . . . . . . ."
    # print(brdStr)
    brdStr += " a b c d e f g h\n"
    my_list_of_lists = [list() for _ in range(8)]
    (rows,columns) = (8, 8)
    for r in rows:
        # brdStr += int(8 - r) + ""
        for c in columns:
            item = my_list_of_lists[r][c]
            brdStr += " ."
        brdStr += "\n"
    print(brdStr)


def write_file():
    board_string = "rnbqkbnrpppppppp................................PPPPPPPPRNBQKBNR"
    file = open('chess_board.txt', mode='w')
    x = file.write(board_string)
    file.close()
    # print(len(board_string))


def read_file_to_list():
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



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # write_file()
    read_file_to_list()
    # print_string()
    # chessboard = Board()
    # chessboard.write_file()
    # chessboard.update_file()
    # chessboard.convert_object()
    # chessboard.pickle_object()
    # chessboard.unpickle_into_object()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
