def common_item(rucksack1, rucksack2):
    common = []
    for item in rucksack1:
        if item in rucksack2:
            common.append(item)
    return set(common)

def priority(items):
    for item in items:
        unicode_item = ord(item)
        if unicode_item <= 90:
            return unicode_item - 38
        else:
            return unicode_item - 96

def main():
    with open("Day3\input.txt") as f:
        input = f.readlines()

    num_elves = len(input)
    groups = []
    group_size = 3

    group_index = 0
    while group_index < int(num_elves/group_size):
        g = 3*(group_index)
        group = [set(input[g].strip()),
                  set(input[g+1].strip()), 
                  set(input[g+2].strip())]
        groups.append(group)
        group_index += 1
    
    count = 0
    for g in groups:
        common_01 = common_item(g[0], g[1])
        common_012 = common_item(common_01, g[2])
        count += priority(common_012)
    
    print(count)


        

if __name__ == "__main__":
    main()