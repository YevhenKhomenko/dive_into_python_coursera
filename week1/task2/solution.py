import sys

lines_num = int(sys.argv[1])

for i in range(lines_num):
	print(("#" * (i + 1)).rjust(lines_num))