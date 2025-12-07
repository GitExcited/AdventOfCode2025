from pathlib import Path
from typing import List

INPUT_PATH = Path("../inputs/day_07.txt")



class Ray:
    def __init__(self,row, column):
        self.row = row
        self.column = column
    def split(self):
        left_ray = Ray(self.row, self.column-1)
        right_ray = Ray(self.row, self.column+1)
        return left_ray, right_ray

class Rays:
    def __init__(self):
        self.rays : List[Ray]= []
        self.collisions = 0

    def move(self, next_line:str):
        current_rays = list(self.rays)
        for ray in current_rays:
            ray.row+=1
            print(f"manifold:{next_line}")
            print(f"Im ray {ray.row},{ray.column}")
            print(f"about to hit: {next_line[ray.column]}")

            if next_line[ray.column] == '^':
                left_ray, right_ray = ray.split()
                self.destroy(ray)
                self.add(left_ray)
                self.add(right_ray)
                self.collisions += 1
        self.merge_rays()
    def merge_rays(self):
        seen = set()
        unique_rays: List[Ray] = []
        for ray in self.rays:
            key = ray.column
            if key not in seen:
                seen.add(key)
                unique_rays.append(ray)
        self.rays = unique_rays
    def add(self, ray:Ray) -> None:
        self.rays.append(ray)
    def destroy(self, ray:Ray):
        for r in self.rays:
            if r.row == ray.row and r.column ==ray.column:
                print("deleted")
                self.rays.remove(r)
                break

def main():
    TOTAL_LINES = 142
    with open(INPUT_PATH) as file:
        first_line = file.readline()
        start_position = first_line.find('S')

    manifold = []
    with open(INPUT_PATH) as file:
        for line in file:
            manifold.append(line)
    print(manifold)
    start_ray = Ray(0, start_position)
    all_rays = Rays()
    all_rays.add(start_ray)
    for i in range(1,TOTAL_LINES):
        all_rays.move(next_line = manifold[i])

    print(all_rays.collisions)

if __name__ =="__main__":
    main()