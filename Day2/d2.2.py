import sys
from pathlib import Path


#   col 1 (oppenent)         col 2 (my score)      
#    Rock = A                   X = Lose
#    Paper = B                  Y = draw 
#    Scissors = C                Z = Win


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
        'A X': lose + scissors,
        'A Y': draw + rock,
        'A Z': win + paper,
        'B X': lose + rock,
        'B Y': draw + paper,
        'B Z': win + scissors,
        'C X': lose + paper,
        'C Y': draw + scissors,
        'C Z': win + rock,
    }

    
    for x in data: 
        score += round[x]
    print(score)


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        roshambo(Path.read_text(file))
    else:
        raise TypeError("This is not a file")