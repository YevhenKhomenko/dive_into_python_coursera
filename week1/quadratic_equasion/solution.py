import sys

a, b, c = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])

d = b ** 2 - 4 * a * c
x1 = (-b + d ** 0.5) / (2 * a)
x2 = (-b - d ** 0.5) / (2 * a) 

print(int(x1))
print(int(x2))