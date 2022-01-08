#!/usr/bin/env python3
"Solves: Day1: Sonar Sweep"

def get_increase_count(nums):
    count = 0
    for i in range(1, len(nums)):
        prev = nums[i - 1]
        curr = nums[i]
        if curr > prev:
            count += 1
    return count

def read(filename):
    input = []
    with open(filename, 'r') as f:
        for line in f:
            for num in line.split():
                input.append(int(num))
    return input

print("result with sample_input: {}".format(get_increase_count(read('sample_input.txt'))))
print("result with input: {}".format(get_increase_count(read('input.txt'))))
