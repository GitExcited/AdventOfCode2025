from pathlib import Path
INPUT_PATH = Path("../../inputs_shanvin/day_04.txt")

def find_accessible_toilet_paper(grid):
    rows=(len(grid))
    col=(len(grid[0]))
    result=0
    directions_check=[(0,1), (0,-1), (1, 0), (1, -1), (1,1), (-1, 0), (-1, -1), (-1, 1)]
    for i in range(rows):
        for j in range(col):
            roll_counter=0
            if grid[i][j]=="@":
                for r, c in directions_check:
                    next_r, next_c=r+i, j+c
                    if (next_r<0 or next_r>=rows or next_c<0 or next_c>=col):
                        continue
                    elif(grid[next_r][next_c]=="@"):
                        roll_counter+=1
                    if roll_counter>=4:
                        break
                if (roll_counter<4):
                    result+=1
    return result


def find_accessible_toilet_paper_P2(grid):
    rows=(len(grid))
    col=(len(grid[0]))
    result=0
    directions_check=[(0,1), (0,-1), (1, 0), (1, -1), (1,1), (-1, 0), (-1, -1), (-1, 1)]
    changes=float("inf")
    while (changes!=0):
        changes=0
        for i in range(rows):
            for j in range(col):
                roll_counter=0
                if grid[i][j]=="@":
                    for r, c in directions_check:
                        next_r, next_c=r+i, j+c
                        if (next_r<0 or next_r>=rows or next_c<0 or next_c>=col):
                            continue
                        elif(grid[next_r][next_c]=="@"):
                            roll_counter+=1
                        if roll_counter>=4:
                            break
                    if (roll_counter<4):
                        grid[i][j]="."
                        result+=1
                        changes+=1
    return result


def main():
    grid=[]
    with open(INPUT_PATH, "r") as f:
        for line in f:
            data=line.strip()
            row=list(data)
            grid.append(row)
        print(find_accessible_toilet_paper_P2(grid))

        

if __name__=="__main__":
    main()