import fileinput
from typing import List

lines = []
for line in fileinput.input():
    lines.append(line.rstrip())

numbers: List[str] = lines[0].split(",")

class Board:
    def __init__(self):
        self.horizontal = []
        self.vertical = {}
        self.complete = False

    def add(self, line):
        self.horizontal.append(line)
        for index in range(len(line)):
            if index not in self.vertical:
                self.vertical[index] = []

            self.vertical[index].append(line[index])

    def remove(self, number):
        for line in self.horizontal:
            if number in line:
                line.remove(number)
                if len(line) == 0:
                    self.complete = True
                    return True

        for index in self.vertical:
            line = self.vertical[index]

            if number in line:
                line.remove(number)
                if len(line) == 0:
                    self.complete = True
                    return True

        return False

    def sum(self):
        return sum(map(lambda line: sum([int(i) for i in line]), self.horizontal))

    def is_complete(self):
        return self.complete

boards = []
board = Board()

for index in range(2, len(lines)):
    line = list(filter(lambda v: v != '', lines[index].split(' ')))

    if len(line) == 0:
        boards.append(board)
        board = Board()
        continue

    board.add(line)

boards.append(board)

total_boards: int = len(boards)
complete_boards: int = 0

for number in numbers:
    for board in boards:
        if not board.is_complete() and board.remove(number):
            complete_boards += 1
            if complete_boards == total_boards:
                print(number, board.sum(), board.sum() * int(number))
                exit(0)
