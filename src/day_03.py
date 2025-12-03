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


sum  =0
def value_of(digits:str)->int:

    value = 0
    for digit in digits:
        value+=int(digit)
    return value

for k in range(0,len(battery_banks)):
    bank = battery_banks[k]
    best_digits = bank[0:12] #take first 12 digits, that's the base case value
    best_value = int(best_digits)

    #We will take one by one,digits after the first 12 to see if it's worth adding them
    for i in range(12,len(bank)):
        check_digit = bank[i]
        new_large_digit = best_digits +check_digit #appends check digit at the end of best digit
        for j in range (0,12): # now 'hide' or remove one digit one by one to see if we can find a better value

            first_half = new_large_digit[0:j]
            second_half = new_large_digit[j + 1:]
            combination = first_half + second_half

            new_value = int(combination)
            if new_value > best_value:
                best_digits = combination
                best_value = new_value

    sum+= best_value
print("Part 2 Answer ⭐")
print(sum)
print("================")
