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
    for r in range(8):
        # brdStr += int(8 - r) + ""
        for c in range(8):
            item = my_list_of_lists[r][c]
            brdStr += " ."
        brdStr += "\n"
    print(brdStr)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # print_string()
    chessboard = Board()
    # chessboard.write_file()
    # chessboard.update_file()
    # chessboard.convert_object()
    chessboard.pickle_object()
    chessboard.unpickle_into_object()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
