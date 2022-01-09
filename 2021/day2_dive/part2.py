#!/usr/bin/env python3

def read(filename):
    with open(filename, 'r') as f:
        return [line.split() for line in f]

def get_position(commands):
    horizontal = 0
    depth = 0
    aim = 0
    for command in commands:
        direction = command[0]
        distance = int(command[1])
        # print("{} {}".format(direction, distance))

        if direction == "forward":
            horizontal += distance
            if aim != 0:
                depth += aim * distance
        elif direction == "down":
            aim += distance
        elif direction == "up":
            aim -= distance
        # print("{} {}".format(horizontal, depth))

    return horizontal * depth

get_position(read('input.txt'))
