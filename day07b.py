from sys import stdin

crabs = [int(x) for x in str(stdin.readlines()[0]).split(",")]


def calc_fuel_usage(current_pos, _desired_pos):
    distance = _desired_pos - current_pos
    fuel = (distance * (distance + 1)) / 2
    return fuel


last_fuel_usage = float('inf')
for desired_pos in range(max(crabs) + 1):
    fuel_usage = sum(map(lambda current_pos: calc_fuel_usage(current_pos, desired_pos), crabs))
    print(desired_pos, fuel_usage)
    if last_fuel_usage < fuel_usage:
        print(int(last_fuel_usage))
        exit(0)
    last_fuel_usage = fuel_usage
