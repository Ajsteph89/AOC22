import sys, string
from pathlib import Path

# split txt file into groups of 3
# find character that is in all 3 parts
# find sum of the characters

def badges(input):
    pack = input.split('\n')
    
    group = list(pack[i:i+3] for i in range(0, len(pack), 3))
    
    total = 0 

    characters = {
            'a': 1,
            'b': 2,
            'c': 3,
            'd': 4,
            'e': 5,
            'f': 6,
            'g': 7,
            'h': 8,
            'i': 9,
            'j': 10,
            'k': 11,
            'l': 12,
            'm': 13,
            'n': 14,
            'o': 15,
            'p': 16,
            'q': 17,
            'r': 18,
            's': 19,
            't': 20,
            'u': 21,
            'v': 22,
            'w': 23,
            'x': 24,
            'y': 25,
            'z': 26,
            'A': 27,
            'B': 28,
            'C': 29,
            'D': 30,
            'E': 31,
            'F': 32,
            'G': 33,
            'H': 34,
            'I': 35,
            'J': 36,
            'K': 37,
            'L': 38,
            'M': 39,
            'N': 40,
            'O': 41,
            'P': 42,
            'Q': 43,
            'R': 44,
            'S': 45,
            'T': 46,
            'U': 47,
            'V': 48,
            'W': 49,
            'X': 50,
            'Y': 51,
            'Z': 52,
        }


    for x in group:
        for y in x:
            for z in y:
                if (z in x[0]) and (z in x[1]) and (z in x[2]):
                    total += characters[z]
                    break
                    

    print(total/3)



if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        badges(Path.read_text(file))
    else:
        raise TypeError("This is not a file")