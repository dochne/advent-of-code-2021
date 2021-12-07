from sys import stdin

fish = [int(x) for x in str(stdin.readlines()[0]).split(",")]

total_days = 80

for days in range(total_days):
    current_fish = len(fish)
    for i in range(current_fish):
        fish[i] -= 1
        if fish[i] == -1:
            fish[i] = 6
            fish.append(8)

print(len(fish))
