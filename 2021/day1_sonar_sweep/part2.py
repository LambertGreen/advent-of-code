#!/usr/bin/env python3
"Solves: Day1: Sonar Sweep"


def read(filename):
    return [int(num) for num in open(filename)]


def get_increase_count(nums):
    window_size = 3
    count = 0
    prev_window_sum = 0
    for i in range(window_size):
        prev_window_sum += nums[i]

    for i in range(window_size, len(nums)):
        curr_window_sum = prev_window_sum - nums[i - window_size] + nums[i]
        if curr_window_sum > prev_window_sum:
            count += 1
        prev_window_sum = curr_window_sum
    return count


print("sample_input: {}".format(get_increase_count(read("sample_input.txt"))))
print("input: {}".format(get_increase_count(read("input.txt"))))
