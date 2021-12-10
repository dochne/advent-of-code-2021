from sys import stdin

crabs = [int(x) for x in str(stdin.readlines()[0]).split(",")]

last_average_distance = 9999999
for x in range(max(crabs) + 1):
    distances = list(map(lambda crab: abs(crab - x), crabs))
    average_distance = sum(distances) / len(crabs)
    if average_distance > last_average_distance:
        print(int(last_average_distance * len(crabs)))
        exit(0)
    last_average_distance = average_distance
