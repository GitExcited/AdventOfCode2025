from pathlib import Path
INPUT_PATH = Path("../../inputs_shanvin/day_07.txt")
from collections import deque, defaultdict
def process_teleporation(grid):
    # find S in top row
    index_initial = 0
    for i in range(len(grid[0])):
        if grid[0][i] == "S":
            index_initial = i
            break

    R, C = len(grid), len(grid[0])

    # queue[col] = number of timelines currently at this column on THIS row
    queue = defaultdict(int)
    queue[index_initial] = 1

    for r in range(R):
        work = deque(queue.keys())

        # resolve all splitter chain reactions on the SAME row
        while work:
            c = work.popleft()
            cnt = queue.get(c, 0)
            if cnt == 0:
                continue

            if grid[r][c] == "^":
                # timelines at the splitter split into left + right
                queue[c] = 0  # particle stops here in all those timelines

                if c - 1 >= 0:
                    was_zero = (queue[c - 1] == 0)
                    queue[c - 1] += cnt
                    if was_zero:
                        work.append(c - 1)

                if c + 1 < C:
                    was_zero = (queue[c + 1] == 0)
                    queue[c + 1] += cnt
                    if was_zero:
                        work.append(c + 1)

        # after row r is stable, the particle moves DOWN one row:
        # columns stay the same, counts stay the same
        queue = defaultdict(int, {c: cnt for c, cnt in queue.items() if cnt != 0})

    # after processing all rows, total timelines = sum of counts
    return sum(queue.values())
            

def main():
    grid=[]
    with open(INPUT_PATH, "r") as f:
        for line in f:
            grid.append(list(line))
    result=process_teleporation(grid)
    print (result)
if __name__=="__main__":
    main()