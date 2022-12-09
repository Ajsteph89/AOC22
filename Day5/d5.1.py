import sys
from pathlib import Path
import re


#turn 'stacks' into list
#use 'directions to pop and append to other lists

def get_stacks(input):
    part = input.split('\n\n')
    set_up = part[0].split('\n')
    # print(set_up)
    for element in set_up:
        parts = element.split('   ')
        print(parts)
        



if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        get_stacks(Path.read_text(file))
    else:
        raise TypeError("This is not a file")