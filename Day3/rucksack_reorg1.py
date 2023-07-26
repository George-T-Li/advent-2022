def split_ruck(rucksack):
    rucksack = rucksack.strip()
    half = int(len(rucksack)/2)
    compartment1 = rucksack[:half]
    compartment2 = rucksack[half:]
    return (set(compartment1), set(compartment2))

def common_item(compartments):
    for item in compartments[0]:
        if item in compartments[1]:
            return item

def priority(item):
    unicode_item = ord(item)
    if unicode_item <= 90:
        return unicode_item - 38
    else:
        return unicode_item - 96

def main():
    with open("Day3\input.txt") as f:
        input = f.readlines()

    total = 0
    for rucksack in input:
        total += priority(common_item(split_ruck(rucksack)))
    print(total)

if __name__ == "__main__":
    main()