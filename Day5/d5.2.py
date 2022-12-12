import sys
from pathlib import Path


def get_stacks(input):
# split initial txt doc into two parts
    initial_stack, instructions = (i.splitlines() for i in input.strip('\n').split('\n\n'))

# creates a dictionary of lists with the keys being the given number of each stack of crates
    stacks = {int(digit):[]for digit in initial_stack[-1].replace(" ", "")}

# Makes a new list of the indexes for the number of each stack of crates
    indexes = [index for index, char in enumerate(initial_stack[-1]) if char != " "]

# starting at the top of the stack, look at each item at the index we have created in indexes, if it is not a blank space add that item to the beggining of the list(value) assigned to the stac(key) in dictionary of stacks
    for string in initial_stack[:-1]:
        stack_num = 1
        for index in indexes:
            if string[index] != " ":
                stacks[stack_num].insert(0, string[index])
            stack_num += 1

#for each line in the instructions list, get rid of the words and black spaces and make a list for each one. Then make each item in the list an integer and not string
    for instruction in instructions:
        instruction = instruction.replace("move", "").replace("from ", "").replace("to ", "").strip().split(" ")
        instruction = [int(i)for i in instruction]
        
        # set each index for the instruction equal to a variable
        crates = instruction[0]
        from_stack = instruction[1]
        to_stack = instruction[2]

        crates_to_remove = stacks[from_stack][-crates:] #find how many crates to move
        stacks[from_stack] = stacks[from_stack][:-crates] #remove crates

        # move crates
        for crate in crates_to_remove:
            stacks[to_stack].append(crate)


    # for each stack print the last value
    answer = ""
    for stack in stacks:
        answer += stacks[stack][-1]

    print(answer)


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        get_stacks(Path.read_text(file))
    else:
        raise TypeError("This is not a file")