from pathlib import Path

INPUT_PATH = Path("../inputs/day_01.txt")
movements = []
with open(INPUT_PATH) as file:
    lines = [line.rstrip() for line in file]
    # Preprocess file into tuples
    for line in lines :
        direction = line[0]
        amount = int(line[1:])
        movements.append((direction,amount))




#Dial begins pointing at 50
class Dial:
    def __init__(self):
        self.pointer = 50
        self.zeros = 0
        self.size = 100 # 100 digits from [ 0, 1, .. , 98, 99]

    def move_left(self, moves):
        self.pointer = (self.pointer - moves)% self.size
        if self.pointer == 0:
            self.zeros+=1

    def move_right (self,moves):
        self.pointer = (self.pointer +moves)% self.size
        if self.pointer == 0:
            self.zeros+=1

    def move_dial(self,moves):
        for move in moves:
            direction = move[0]  # L or R
            amount = move[1]
            if direction == 'L':
                self.move_left(amount)
            else:
                self.move_right(amount)

class SpecialDial (Dial):
    def __init__(self):
        super().__init__()

    def passes_by_zero_right(self, start, moves):

        # Special case: starting at 0 and moving right
        if start == 0:
            repetitions = moves // self.size
            return repetitions

        # Normal case: starting at position > 0
        if start + moves < self.size:
            return 0

        # We reach or pass 0 at least once
        moves_to_zero = self.size - start
        remaining = moves - moves_to_zero
        repetitions = 1 + (remaining // self.size)

        return repetitions

    def passes_by_zero_left(self, start, moves):

        if start == 0:
            repetitions = moves // self.size
            return repetitions

        if start > moves:
            return 0

        remaining = moves - start
        repetitions = 1 + (remaining // self.size)
        return repetitions

    def move_left(self,moves):

        passed_zeros = self.passes_by_zero_left(self.pointer, moves)
        self.zeros += passed_zeros
        self.pointer = (self.pointer - moves) % self.size

    def move_right(self,moves):

        self.zeros += self.passes_by_zero_right(self.pointer,moves)
        self.pointer = (self.pointer +moves)% self.size

if __name__ == "__main__":

    # PART 1
    dial = Dial()
    dial.move_dial(movements)
    print("Part 1 Answer ⭐")
    print(dial.zeros)
    print("================")

    #PART 2
    dial = SpecialDial()
    dial.move_dial(movements)
    print( "Part 2 Answer ⭐")
    print(dial.zeros)
    print(f"Dial at {dial.pointer}")
    print( "======")



