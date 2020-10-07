# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def print_string():
    brdStr = ""
    # brdStr += " . . . . . . . ."
    # print(brdStr)
    brdStr += " a b c d e f g h\n"
    my_list_of_lists = [list() for _ in range(8)]
    for r in range(8):
        # brdStr += int(8 - r) + ""
        for c in range(8):
            item = my_list_of_lists[r][c]
            brdStr += " ."
        brdStr += "\n"
    print(brdStr)


def print_chessboard():

    board_string = ""
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
    board_string += "a b c d e f g h\n"
    print(board_string)
    for column in board:
        for item in column:
            print(item, end=" ")
        print()

    print("\n" + board_string)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # print_string()
    print_chessboard()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
