

def read_columns(path):
    with open(path, 'r') as file:
        columns = file.readlines()
        columns = list(map(str.rstrip, columns))
    return columns


def pos(arr):
    return sum(arr)


def neg(arr):
    return len(arr) - sum(arr)
