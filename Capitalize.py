#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve():
        s=input()
        s=list(s.split(" "))
        for i in range(len(s)):
            s[i]=str(s[i]).capitalize()
        return " ".join(s)