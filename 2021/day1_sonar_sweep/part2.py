#!/usr/bin/env python3
"Solves: Day1: Sonar Sweep"

def get_increase_count(nums):
    window_size = 3
    count = 0
    prev_window_sum = 0;
    for i in range(window_size):
        prev_window_sum += nums[i]

    print("{} -  no previous sum".format(prev_window_sum))

    for i in range(window_size, len(nums)):
        curr_window_sum = prev_window_sum - nums[i - window_size] + nums[i]
        if curr_window_sum > prev_window_sum:
            count += 1
            print("{} - increased".format(curr_window_sum))
        else:
            print("{} - decreased".format(curr_window_sum))
        prev_window_sum = curr_window_sum
    return count

def read(filename):
    with open(filename, 'r') as f:
        return [int(x) for x in f.readlines()]

print("result with sample_input: {}".format(get_increase_count(read('sample_input.txt'))))
print("result with input: {}".format(get_increase_count(read('input.txt'))))
