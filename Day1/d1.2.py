import sys
from pathlib import Path


def get_calories(input):
    data = (input.split('\n'))
    count = 0
    calories = []
    for x in data:
        if x != '':
            count += int(x)
        if x == '':
            calories.append(count)
            count = 0
    
    calories.append(count)
    
    calories.sort(reverse=True)
    
    top_three = sum(calories[:3])
    
    print(top_three)


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        get_calories(Path.read_text(file))
    else:
        raise TypeError("This is not a file")