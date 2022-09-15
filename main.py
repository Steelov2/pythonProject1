import math

h = int(input('Enter the height of a rectangle:'))
w = int(input('Enter the width of a rectangle:'))
print("The area of a rectangle with height: {0} and width: {1} is {2}".format(h, w, h * w))

rad = int(input('Enter the radius of a circle:'))
print("The are of the circle with radius: {0} is {1} ".format(rad, round(math.pi * rad * rad, 4)))

height = int(input("Enter the height of the right triangle:"))
base = int(input("Enter the base of the right triangle:"))
print("The area of th right triangle with height:{0} and base {1} is {2}".format(height, base, 0.5 * height * base))
print("The perimeter of th right triangle with height:{0} and base {1} is {2}".format(height, base,
                                                                                      height + base + math.pow(
                                                                                          height * height + base * base,
                                                                                          0.5)))
