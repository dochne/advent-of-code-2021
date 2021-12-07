from array import array
from sys import stdin

fish = [int(x) for x in str(stdin.readlines()[0]).split(",")]

by_number = array('i', (0,) * 9)
for timer in fish:
    by_number[timer] += 1

total_days = 256
for days in range(total_days):
    next_iteration = array('Q', (0,) * 9)
    for timer in range(len(by_number)):
        if timer == 0:
            next_iteration[6] += by_number[timer]
            next_iteration[8] += by_number[timer]
        else:
            next_iteration[timer - 1] += by_number[timer]
    by_number = next_iteration

print(sum(by_number))
exit(0)
