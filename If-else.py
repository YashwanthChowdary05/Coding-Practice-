
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0:
        print("Weired")
    elif n >= 2 and n<=5:
        print("Not Weired")
    elif n >= 6 and n <= 20:
        print("Weired")
    elif n > 20:
        print("Not Weired")