def overlap(pair):
    elves = (pair.strip()).split(",")
    elf1 = list(map(int, elves[0].split("-")))
    elf2 = list(map(int, elves[1].split("-")))

    if elf1[0] <= elf2[0] and elf1[1] >= elf2[0]:
        return 1
    elif elf1[0] >= elf2[0] and elf2[1] >= elf1[0]:
        return 1
    else:
        return 0

def main():
    with open("Day4\input.txt") as f:
        input = f.readlines()

    count = 0
    for pair in input:
        count += overlap(pair)
    print(count)

if __name__ == "__main__":
    main()