from pathlib import Path

INPUT_PATH  = Path("../inputs/day_04.txt")
TOTAL_LINES = 0
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
for row in grid:
    TOTAL_LINES+=1
sum = 0

changed = False
first_time = True

# while changed or first_time:
#     if first_time:
#         first_time = False
#     changed = False
i = 1
j = 1
while i < (TOTAL_LINES-1):
    while j< (len(grid[i])-1):
        current= grid[i][j]
        if current== '@':
            count = 0 #Number of rolls around
            top = i-1
            bottom = i+1
            left = j-1
            right = j+1
            coordinates_around = [grid[top][left], grid[top][j], grid[top][right],
                                  grid[i][left],              grid[i][right],
                                  grid[bottom][left],grid[bottom][j], grid[bottom][right]]
            for coordinate in coordinates_around:
                if coordinate =='@':count+=1
            if count<4:
                sum +=1
                grid[i][j]= "."
                print(f"Found one that got switched, we used to be at {i},{j}")
                i = top
                j = left-1 #Move pointer to top left and retry
                print(f"Now we at {i},{j}")


        j+=1
    i+=1
    j=1

print(sum)
