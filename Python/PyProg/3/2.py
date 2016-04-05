# Write a program that calculates the cost per square inch of a circular pizza,
# given its diameter and price. The formula for area is A = (pi)r^2
import math

def main():
    diameter = input("Diameter in inches: ")
    price = input("Price: ")
    radius = diameter / 2.0

    area = math.pi * radius ** 2
    costPerSquareInch = round(price / area, 2)

    print "Given your diamter and price of the pizza, the pizza costs $" + \
        str(costPerSquareInch) + " per square inch."

main()
