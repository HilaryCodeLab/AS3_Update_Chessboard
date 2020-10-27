from typing import List
from BoardState import BoardState


file_name ='chess_board.txt'

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def write_file():
    board_string = "rnbqkbnrpppppppp................................PPPPPPPPRNBQKBNR"
    file = open('chess_board.txt', mode='w')
    x = file.write(board_string)
    file.close()
    # print(len(board_string))


def read_file_to_list(file_name):
    file = open(file_name, mode='r')
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


def update_chess_table():
    file = open('chess_board.txt', mode='r+')
    file.seek(9)
    user_input = input("place your move: ")
    file.write(user_input)
    file.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    # write_file()
    # read_file_to_list(file_name)
    # update_chess_table()
    # read_file_to_list(file_name)
    board = BoardState()
    # board.algebraic_notation()
    board.algebraic_notation()






