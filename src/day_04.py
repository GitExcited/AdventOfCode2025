from pathlib import Path

INPUT_PATH  = Path("../inputs/day_04.txt")
TOTAL_LINES = 139 # From the .txt file, could've also written code to count them
with open(INPUT_PATH) as file:
    grid = [[el for el in line.rstrip()] for line in file]
    blank = ['.' for i in range(len(grid[0])) ]
    grid.insert(0,blank) # First line is blanks
    grid.append(blank)#Laast linke is blanks
    #Put blanks at start and end of each line
    for line in grid:
        line.insert(0,'.')
        line.append('.')
    #Basically transforming the original grid with a padding of '.' all around

sum = 0
for i in range(1,TOTAL_LINES-1):
    print(f"i{i}")
    for j in range(1,len(grid[i])-1):
        print(f"j{j}")
        current= grid[i][j]
        if current!= '@': continue
        count = 0 #Number of rolls around
        top = i-1
        bottom = i+1
        left = j-1
        right = j+1
        coordinates_around = [grid[top][left], grid[top][j], grid[top][right],
                              grid[i][left],              grid[i][right],
                              grid[bottom][left],grid[bottom][j], grid[bottom][right]]

        print(coordinates_around)
        for coordinate in coordinates_around:
            if coordinate =='@':count+=1
        if count<4:
            sum +=1

print(sum)
