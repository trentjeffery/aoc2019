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

#print(part1())

def CalculateTotalFuelToLaunch(moduleMass):
    sum = 0
    nextFuel = CalculateFuelToLaunch(moduleMass)
    while nextFuel > 0:
        sum += nextFuel
        nextFuel = CalculateFuelToLaunch(nextFuel)
    return sum

print(CalculateTotalFuelToLaunch(14))
print(CalculateTotalFuelToLaunch(1969))
print(CalculateTotalFuelToLaunch(100756))

def part2():
     with open("input.XSCORE.txt") as input_file:
        sum = 0
        for line in input_file:
            moduleMass = int(line)
            sum += CalculateTotalFuelToLaunch(moduleMass)
        print(sum)

part2()