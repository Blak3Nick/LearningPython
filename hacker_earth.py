n = input()
longest = 0
longest_loc = [0, 0]
def calc_string(string, start):
    while(assess_string(string, start) != len(string)):



def assess_string(string, start):
    location = 0
    length = 0
    for i in range(start, len(string)-1):
        a = string[i]
        if (i + 1) != (len(string)):
            b = string[i + 1]
        else:
            b = a
        if a != b:
            length += 1
        else:
            if length > longest:
                longest = length
                longest_loc = []

    return location





