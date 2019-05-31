import math
import random

def IsInCircle(x,y):
    return (math.sqrt(x**2+y**2) < 1)

def find():
    all_dots = 0
    incircle_dots = 0
    pi = 0
    while round(pi,2) != 3.14:
        x = random.random()
        y = random.random()
        all_dots += 1
        if IsInCircle(x,y):
           incircle_dots += 1
        pi = incircle_dots / all_dots * 4
    print(all_dots)

find()