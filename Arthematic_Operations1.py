# When users post an update on social media,such as a URL, image, status update etc., other users in their network are able to view this new post on their news feed. Users can also see exactly when the post was published, i.e, how many hours, minutes or seconds ago.
# Since sometimes posts are published and viewed in different time zones, this can be confusing. You are given two timestamps of one such post that a user can see on his newsfeed in the following format:
# Day dd Mon yyyy hh:mm:ss +xxxx
# Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.

# Input Format
# The first line contains T, the number of testcases.
# Each testcase contains 2 lines, representing time t1 and time t2.

# Constraints
# Input contains only valid timestamps.

# Output Format:
# Print the absolute difference (t1-t2) in seconds.

#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

def time_delta(t1, t2):
    t1_obj = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    t2_obj = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    return str(abs(int((t1_obj - t2_obj).total_seconds())))

if __name__ == '__main__':
    # Instead of opening a file using OUTPUT_PATH, redirect stdout
    with open('output.txt', 'w') as fptr:  # Open a file named output.txt
        t = int(input())

        for t_itr in range(t):
            t1 = input()
            t2 = input()

            delta = time_delta(t1, t2)

            fptr.write(delta + '\n')

    print("Output written to output.txt") # Optional confirmation message22




