import math
import array

def CalculateFuelToLaunch(mass):
    return math.floor(mass/3) - 2

'''
def SumFuelReqs(array):
    sum = 0
    for val in array
        sum += CalculateFuelToLaunch(val)
    return sum'''

def part1():
    with open("input.XSCORE.txt") as input_file:
        sum = 0
        for line in input_file:
            val = int(line)
            sum += CalculateFuelToLaunch(val)
        print(sum)

print(part1())