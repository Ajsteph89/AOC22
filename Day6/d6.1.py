import sys
from pathlib import Path



# starting at the first letter see if that letter and the next three are unique if not move up to the next letter

def connect_four(input):
    window_size = 4
    for i in range(len(input)-window_size +1):
        four = (input[i: i + window_size])
        if len(set(four)) == len(four):
            print(four)
            print(i+4)
            break
    


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        connect_four(Path.read_text(file))
    else:
        raise TypeError("This is not a file")