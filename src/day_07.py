from pathlib import Path
from typing import List

INPUT_PATH = Path("../inputs/day_07.txt")



class Ray:

    def __init__(self,row, column, energy= 1):
        self.row = row
        self.column = column
        self.energy = energy #How many rays this ray represents

    def split(self):
        left_ray = Ray(self.row, self.column-1, self.energy)
        right_ray = Ray(self.row, self.column+1, self.energy)
        return left_ray, right_ray

    def __eq__(self,other):
        return self.row == other.row and self.column ==other.column

class Rays:

    def __init__(self):
        self.rays : List[Ray]= []
        self.collisions = 0 #For part I only

    def move(self, next_line:str):
        current_rays = list(self.rays)
        for ray in current_rays:
            ray.row+=1
            if next_line[ray.column] == '^':
                left_ray, right_ray = ray.split()
                self.destroy(ray)
                self.add(left_ray)
                self.add(right_ray)
                self.collisions += 1
        self.special_merge() #Merge for part II
        # self.merge_rays() # Not used for part II

    def special_merge(self):
        seen = set()
        unique_rays: List[Ray] = []
        for ray in self.rays:
            key = ray.column
            if key in seen:
                for repeated_ray in unique_rays:
                    if ray == repeated_ray:
                        repeated_ray.energy += ray.energy
                        break #once we give our energy to another ray, disappear
            if key not in seen:
                seen.add(key)
                unique_rays.append(ray)

        self.rays = unique_rays

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
                self.rays.remove(r)
                break

    def total_energy(self)-> int:
        energy_total = 0
        for ray in self.rays:
            energy_total+= ray.energy
        return energy_total

def main():
    TOTAL_LINES = 142
    manifold = []

    with open(INPUT_PATH) as file:
        start_position = file.readline().find('S')

    with open(INPUT_PATH) as file:
        for line in file:
            manifold.append(line)

    start_ray = Ray(0, start_position)
    all_rays = Rays()
    all_rays.add(start_ray)

    for i in range(1,TOTAL_LINES): all_rays.move(next_line = manifold[i])

    print(all_rays.total_energy())

if __name__ =="__main__":
    main()