class Board:
    def __init__(self, rows):
        self.rows = []
        for i in range(0,5):
            self.rows.append(rows[i].split())

    def has_bingo(self):
        # Check horizontal wins
        for row in self.rows:
            if row[0] == "X" and \
               row[1] == "X" and \
               row[2] == "X" and \
               row[3] == "X" and \
               row[4] == "X":
                return True

        # Check vertical wins
        for i in range(0,5):
            if self.rows[0][i] == "X" and \
               self.rows[1][i] == "X" and \
               self.rows[2][i] == "X" and \
               self.rows[3][i] == "X" and \
               self.rows[4][i] == "X":
                return True

        return False

    def mark(self, number):
        for row in self.rows:
            for col in range(0,5):
                if row[col] == number:
                    row[col] = 'X'

    def score(self):
        score = 0
        for row in self.rows:
            for col in range(0,5):
                if row[col] != 'X':
                    score = score + int(row[col])
        return score

    def __str__(self):
        s = ""
        for row in self.rows:
            s = s + " ".join(row)
            s = s + '\n'

        return s.strip()

boards = []
called_numbers = []

def play(): 
    for number in called_numbers:
        next_round = []
        for board in boards:
            if not board.has_bingo():
                board.mark(number)
                if board.has_bingo():
                    print("\nBINGO!!!!")
                    print(board)
                    print("Score", board.score())
                    print("Winning Number", number)
                    print("Score * Number =", board.score() * int(number))

with open("input4.txt", "r") as file:
    called_numbers = file.readline().strip().split(',')

    board_list = file.read().strip().split('\n\n')

    for board in board_list:  
        rows = board.split('\n')
        boards.append(Board(rows))

play()