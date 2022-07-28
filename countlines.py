import sys
from functools import reduce
def counter():
    """
    Counts the number of lines in a file.
    """
    print("[", end='')
    for arg in sys.argv[1:]:
        count = count_lines_in_file(arg)
        if count != -1:
            print(f"('{arg}', {count})", end=',')
    print("]")
    print("le nombre total de ligne est {}".format(total_lines()))

def count_lines_in_file(filename):
    """
    Counts the number of lines in a file.
    """
    try: 
        with open(filename) as f:
            return sum(1 for line in f)
    except FileNotFoundError:
        return -1


def total_lines():
    """
    Counts the number of lines in all files.
    """
    return reduce(lambda x, y : x + y , [count_lines_in_file(arg) for arg in sys.argv[1:]])
    

if __name__ == '__main__':
    counter()