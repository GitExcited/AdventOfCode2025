from pathlib import Path
import csv
from typing import List

INPUT_PATH = Path("../inputs/day_02.txt")
product_ids = []
with open(INPUT_PATH)  as file:
    reader = csv.reader(file)
    for row in reader:
        for el in row:
            product_ids.append(el)

def is_valid_id(_id:str) -> bool :
    #Assumption: if id is odd, it can't be a duplicate of 2 numbers: 313 is not an invalid id for example. 3113 is.
    length = len(_id)
    if length%2 != 0 :
        return True
    elif _id[0: length// 2] == _id[length//2:]:
        return False
    return True

def find_invalid(start:int, end:int)->List[int]:
    invalid= []
    for i in range(start, end+1):
        if not is_valid_id(str(i)):
            invalid.append(i)
    return invalid

sum = 0
for product_id in product_ids:
    both_ids = product_id.split("-")
    firstID = both_ids[0]
    lastID = both_ids[1]
    invalid_IDs =find_invalid(int(firstID),int(lastID))
    for invalid_id in invalid_IDs:
        sum+=invalid_id

print(sum)

