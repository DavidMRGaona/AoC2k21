#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import namedtuple
import concurrent.futures


# Global Stuff
class Board:
    counter = 0

    def __init__(self, numbers, size=5):
        self.no = Board.counter
        Board.counter += 1
        self.numbers = numbers
        self._numbers_set = set(numbers)
        self._marked = set()
        self._size = size
        self._remove_mark = False

    def mark(self, n):
        if n in self._numbers_set:
            self._marked.add(n)

    def _check_row(self, i):
        return all([self.numbers[i * self._size + j] in self._marked for j in range(self._size)])

    def _check_col(self, j):
        return all([self.numbers[i * self._size + j] in self._marked for i in range(self._size)])

    def check(self):
        return any([self._check_row(i) for i in range(self._size)]) or \
               any([self._check_col(j) for j in range(self._size)])

    def score(self):
        return sum(self._numbers_set - self._marked)

    def remove(self):
        # Not an actual removal
        self._remove_mark = True

    @property
    def removed(self):
        return self._remove_mark


def _read_board(fp):
    board = []
    for _ in range(5):
        row = fp.readline()
        board += [int(row[n:(n + 2)]) for n in range(0, 15, 3)]
    return Board(board)


def read_bingo(case):
    with open(f'{case}') as f:
        numbers = [int(x) for x in f.readline().split(',')]

        boards = []
        while f.readline() != '':  # exploit empty line between boards LUL
            boards.append(_read_board(f))

        return numbers, boards


WinnerMove = namedtuple('WinnerMove', ['count', 'score', 'number'])


def play_board(numbers, board):
    for i, n in enumerate(numbers):
        board.mark(n)
        if board.check():
            return WinnerMove(i, board.score() * n, n)


def play_bingo(case):
    numbers, boards = read_bingo(case)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_moves = [executor.submit(play_board, numbers, b) for b in boards]

    winner_moves = [wm for wm in concurrent.futures.as_completed(future_moves)]

    return [wm.result() for wm in winner_moves]


# Part 1. Execution
print('Part 1.', end=' ')
scores = play_bingo('input')
first = min(scores, key=lambda x: x.count)
print(f'Bingo Final Score: {first.score}')
print('Done!')

# Part 2print('Part 2.', end=' ')
scores = play_bingo('input')
last = max(scores, key=lambda x: x.count)
print(f'Last winner bingo Final Score: {last.score}')
print('Done!')
