import fileinput
from typing import Optional

depths = []
for line in fileinput.input():
    depths.append(int(line.rstrip()))

prev_sum: Optional[int] = None
num_increased: int = 0
for index in range(0, len(depths)):
    cur_sum = sum(depths[index: index + 3])
    if prev_sum is not None and cur_sum > prev_sum:
        num_increased += 1

    prev_sum = cur_sum

print(num_increased)
