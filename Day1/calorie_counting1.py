def main():
    with open("Day1\input.txt") as f:
        input = f.readlines()

    count = 0
    most = 0

    for item in input:
        if item == "\n":
            most = max(most, count)
            count = 0
        else:
            count += int(item)
    
    print(most)

if __name__ == "__main__":
    main()