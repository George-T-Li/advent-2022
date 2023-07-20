def score_rps(opp, you):
    if you == 'X':
        scoreX = {'A':4, 'B':1, 'C':7}
        return scoreX[opp]
    elif you == 'Y':
        scoreY = {'A':8, 'B':5, 'C':2}
        return scoreY[opp]
    elif you == 'Z':
        scoreZ = {'A':3, 'B':9, 'C':6}
        return scoreZ[opp]

def main():
    with open("Day2\input.txt") as f:
        input = f.readlines()

    score = 0
    for round in input:
        opp = round[0]
        you = round[2]
        score += score_rps(opp, you)
    
    print(score)

if __name__ == "__main__":
    main()