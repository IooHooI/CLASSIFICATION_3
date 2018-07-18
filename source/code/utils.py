import pickle


def read_columns(path):
    with open(path, 'r') as file:
        columns = file.readlines()
        columns = list(map(str.rstrip, columns))
    return columns


def pos(arr):
    return sum(arr)


def neg(arr):
    return len(arr) - sum(arr)


def save_obj(obj, path):
    with open(path, 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_obj(path):
    with open(path, 'rb') as f:
        return pickle.load(f)
