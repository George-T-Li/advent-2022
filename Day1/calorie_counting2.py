def main():
    with open("Day1\input.txt") as f:
        input = f.readlines()

    inventory = []
    count = 0

    for item in input:
        if item == "\n":
            inventory.append(count)
            count = 0
        else:
            count += int(item)
    
    print(sum(sorted(inventory)[-3:]))

if __name__ == "__main__":
    main()