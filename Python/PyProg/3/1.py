# Write a program to calculate the volume and surface area of a sphere from
# its radius, given as input. Here are some formulas that might be useful:
#                   V = 4/3(pi)r^3
#                   A = 4(pi)r^2
import math

def main():
    radius = input("Please enter a radius: ")
    print "You entered " + str(radius) + " as your radius."

    volume = round((4.0 / 3.0) * math.pi * radius ** 3, 2)
    print "Given your radius, the volume of your sphere is " + str(volume) + "."

    area = round(4 * math.pi * radius ** 2, 2)
    print "Given your radius, the surface area of your sphere is " + str(area) + "."

main()
