from pathlib import Path

INPUT_PATH  = Path("../inputs/day_04.txt")
TOTAL_LINES = 137 # From the .txt file, could've also written code to count them
with open(INPUT_PATH) as file:

    grid = [[el for el in line] for line in file]



for i in range(0,TOTAL_LINES):
    for j in range(0,len(grid[i])):
        count = 0 #Number of rolls around
        top = i-1
        bottom = i+1
        left = j-1
        right = j+1
        set_combinaisons = {}
        if i>0:
                #don't check top
        if j==0:
            #don't check left
        if i== TOTAL_LINES-1:
            #don't check bottom
        if j== len(grid[i])-1
            #don't check right

        # top
        if i>0:
            if grid[i-1][j] == '@':count+=1

        # top right
            if j< len(grid[i])-1:
                if grid[i-1][j+1] == '@':count+=1
        # top left
            if j> 0:
                if grid[i - 1][j - 1] == '@': count += 1

        # right
        if j< len(grid[i])-1:
            if grid[i][j+1]== '@':count+=1
        # left
        if j> 0:
            if grid[i][j-1]== '@':count+=1

        # bottom
        # bottom right
        # bottom left
print(grid[0])
