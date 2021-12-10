#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import namedtuple
from dataclasses import dataclass


# Day 2. Global Stuff
def read_course(case):
    with open(f'{case}') as f:
        course = [Cmd(*line.split(' ')) for line in f.read().splitlines()]
    return course


Cmd = namedtuple('Cmd', ['dir', 'qty'])


def _pos_curried_add(self, y):
    self.pos += y


def _depth_curried_add(self, y):
    self.depth += y


def _depth_curried_sub(self, y):
    self.depth -= y


def _aim_curried_add(self, y):
    self.aim += y


def _aim_curried_sub(self, y):
    self.aim -= y


def _depth_curried_op(self, y):
    self.pos += y
    self.depth += self.aim * y


class Course:
    def __init__(self, pos=0, depth=0, aim=0):
        self.coords = {'pos': pos, 'depth': depth, 'aim': aim}

    @property
    def pos(self):
        return self.coords['pos']

    @pos.setter
    def pos(self, x):
        self.coords['pos'] = x

    @property
    def depth(self):
        return self.coords['depth']

    @depth.setter
    def depth(self, x):
        self.coords['depth'] = x

    @property
    def aim(self):
        return self.coords['aim']

    @aim.setter
    def aim(self, x):
        self.coords['aim'] = x

    def checksum(self, cmds):
        op_builder = {
            'forward': self.go_forward,
            'up': self.go_up,
            'down': self.go_down
        }
        for cmd in cmds:
            op = op_builder[cmd.dir]
            op(self, int(cmd.qty))

        return self.pos * self.depth


# Part 1
print('Part 1...', end=' ')
course = Course(0, 0, 0)
course.go_forward = _pos_curried_add
course.go_down = _depth_curried_add
course.go_up = _depth_curried_sub
course.coords = {'pos': 0, 'depth': 0, 'aim': 0}
print('Done!')
chk = course.checksum(read_course('input'))
print(f'Found checksum: {chk}')

# Part 2
print('Part 2...', end=' ')
course = Course(0, 0, 0)
course.go_forward = _depth_curried_op
course.go_down = _aim_curried_add
course.go_up = _aim_curried_sub
course.coords = {'pos': 0, 'depth': 0, 'aim': 0}
print('Done!')
chk = course.checksum(read_course('input'))
print(f'Found checksum: {chk}')
