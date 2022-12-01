import sys
from pathlib import Path



def get_calories(input):
    data = input.split('/n/n')
    print(data)
    count = 0
    for x in data:
        if x != '/n/n':
            count 

        print(count)







if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        get_calories(Path.read_text(file))
    else:
        raise TypeError("This is not a file")