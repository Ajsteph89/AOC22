import sys
from pathlib import Path


#   col 1 (oppenent)         col 2 (my score)      
#    Rock = A = 1pt          Rock = X = 1pt
#    Paper = B = 2pt         Paper = Y = 2pt
#    Scissors = C = 3pt      Scissors = Z = 3pt


def roshambo(input):
    data = input.split('\n')
    
    win = 6
    draw = 3
    lose = 0

    rock = 1
    paper = 2
    scissors = 3

    score = 0

    round = {
        'A X': draw + rock,
        'A Y': win + paper,
        'A Z': lose + scissors,
        'B X': lose + rock,
        'B Y': draw + paper,
        'B Z': win + scissors,
        'C X': win + rock,
        'C Y': lose + paper,
        'C Z': draw + scissors,
    }

    for x in data: 
        if x in data:
            score += round[x]
    print(score)

if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        roshambo(Path.read_text(file))
    else:
        raise TypeError("This is not a file")