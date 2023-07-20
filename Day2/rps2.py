def score_rps(opp, result):
    score = {'A':0, 'B':1, 'C':2}
    if result == 'X':
        return 0 + (score[opp]-1) % 3 + 1
    elif result == 'Y':
        return 3 + score[opp] + 1
    elif result == 'Z':
        return 6 + (score[opp]+1) % 3 + 1

def main():
    with open("Day2\input.txt") as f:
        input = f.readlines()

    score = 0
    for round in input:
        opp = round[0]
        result = round[2]
        score += score_rps(opp, result)
        
    
    print(score)

if __name__ == "__main__":
    main()