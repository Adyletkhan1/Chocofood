#!/bin/python3

import math
import os
import random
import re
import sys


def solve():
        string= input()
        string=list(string.split(" "))
        for i in range(len(string)):
            string[i]= str(string[i]).capitalize()
        return " ".join(string)
