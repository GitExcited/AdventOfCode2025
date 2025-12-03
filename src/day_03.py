from pathlib import Path
from typing import List

INPUT_PATH = Path("../inputs/day_03.txt")

battery_banks:List[str] = [ ]
with open(INPUT_PATH) as file:
    for line in file:
        battery_banks.append(line.strip())


# best_indices: [int,int] = [0,0]
sum = 0
for k in range(0,len(battery_banks)):
    best_value = 0
    bank = battery_banks[k]
    # Analyse each bank ( line) to find best value and indices
    for i in range(0,len(bank)):
        for j in range (i+1, len(bank)):
            current_value= int(bank[i])*10 + int(bank[j])
            if current_value>best_value:
                best_value = current_value
                # best_indices = [i,j]
    sum+=best_value

print("Part 1 Answer ⭐")
print(sum)
print("================")


