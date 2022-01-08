#!/usr/bin/env python3
"Solves: Day1: Sonar Sweep"

def read(filename):
    return [int(num) for num in open(filename)]

def get_increase_count(nums):
    count = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            count += 1
    return count

print("result with sample_input: {}".format(get_increase_count(read('sample_input.txt'))))
print("result with input: {}".format(get_increase_count(read('input.txt'))))
