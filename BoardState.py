TEAM_WHITES = 1
TEAM_BLACKS = -1
FILE_NAMES = ["a", "b", "c", "d", "e", "f", "g", "h"]
RANK_NAMES = ["1", "2", "3", "4", "5", "6", "7", "8"]
SQUARE_NAMES = [f + r for r in RANK_NAMES for f in FILE_NAMES]

class BoardState:

    def __init__(self, repr=list('HNBQABNH' + 'P' * 8 + '.' * 32 + 'p' * 8 + 'hnbqabnh'),  trait='w'):
        self._repr = repr
        self.trait = trait

    def team(self):
        return print(TEAM_WHITES) if self.trait == 'w' else TEAM_BLACKS

    def pick_team(self):
        user_input = input("pick a team: Black or White: ")
        if user_input == "white" or "w":
            print("you are on white team")
            return TEAM_WHITES
        else:
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

    def get_team(self, i, j):
        p = self._repr[j * 8 + i]
        if p == '.':
            return 0
        elif p in 'PRHNBQAZ':
            print("white")
            return TEAM_WHITES
        else:
            print("black")
            return TEAM_BLACKS

    def is_same_team(self, i, j, team):
        possibleparts = 'PRHNBQAZ' if team == TEAM_WHITES else 'prhnbqaz'
        return self._repr[j * 8 + i] in possibleparts

    def is_pawn(self):
        part = "P" if TEAM_WHITES else "p"
        print(part)


if __name__ == '__main__':
    board = BoardState()
    board.team()
    # board.team_str()
    # board.pick_team()
    # board.get_team(5,6)
    board.is_same_team(0, 0, -1)
    board.is_pawn()
