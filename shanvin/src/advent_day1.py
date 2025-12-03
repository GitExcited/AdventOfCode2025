def check_0(current, line):
    direction = line[0]
    steps = int(line[1:])
    pos_neg = 1 if direction == "R" else -1

    raw = current + pos_neg * steps         # unwrapped final position
    first = current + pos_neg               # first clicked position

    lo = min(first, raw)
    hi = max(first, raw)

    # number of multiples of 100 between lo and hi (inclusive)
    resets = (hi // 100) - ((lo - 1) // 100)

    current = raw % 100                     # wrap back onto 0–99 dial
    return current, resets


def main():
    path = r"C:\Users\eohsula\OneDrive - Ericsson\Documents\input.txt"
    current = 50
    count_0 = 0

    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            current, resets = check_0(current, line)
            count_0 += resets     # do NOT also check current == 0 here

    print(count_0)


if __name__ == "__main__":
    main()
