from pathlib import Path
INPUT_PATH = Path("../../inputs_shanvin/day_07.txt")
from collections import deque
def process_teleporation(grid):
    index_initial = 0
    for i in range(len(grid[0])):
        if grid[0][i] == "S":
            index_initial = i
            break

    queue = {index_initial}   # reachable columns (beams merge)
    counter = 0               # number of splits

    R, C = len(grid), len(grid[0])

    for r in range(R):
        work = deque(queue)
        while work:
            c = work.popleft()
            if c not in queue:
                continue

            if grid[r][c] == "^":
                counter += 1
                queue.remove(c)

                if c - 1 >= 0 and (c - 1) not in queue:
                    queue.add(c - 1)
                    work.append(c - 1)

                if c + 1 < C and (c + 1) not in queue:
                    queue.add(c + 1)
                    work.append(c + 1)

    return counter
            

def main():
    grid=[]
    with open(INPUT_PATH, "r") as f:
        for line in f:
            grid.append(list(line))
    result=process_teleporation(grid)
    print (result)
if __name__=="__main__":
    main()