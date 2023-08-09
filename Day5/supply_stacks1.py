def main():
    with open("Day5\input.txt") as f:
        input = f.readlines()

    #build stacks
    stacks = {key: [] for key in range(1, 10)}

    while True:
        row = input.pop(0)
        line = row.split()
        if line[0] == "1":
            input.remove(input[0]) #remove newline
            break

        for index, crate in enumerate(line):
            label = crate[1]
            if label != '0':
                stacks[index+1].insert(0, label)

    #arrange crates
    for instruction in input:
        r = parse_inst(instruction)
        quantity = r[0]
        fr = r[1]
        to = r[2]
        l = []
        for i in range(quantity):
            l.append(stacks[fr].pop())
        stacks[to].extend(l)

    print(stacks)
    

def parse_inst(step: str):
    l = step.split()
    quantity = int(l[1])
    from_crate = int(l[3])
    to_crate = int(l[5])
    return quantity, from_crate, to_crate

if __name__ == "__main__":
    main()