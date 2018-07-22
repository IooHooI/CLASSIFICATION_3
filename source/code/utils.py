import pickle
from imblearn.pipeline import Pipeline
from source.code.ItemSelector import ItemSelector
from source.code.MyLabelBinarizer import MyLabelBinarizer


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


def generate_pipeline(column):
    return (column, Pipeline([
        ('choose', ItemSelector(column)),
        ('binarize', MyLabelBinarizer())
    ]))


def generate_features_names(bin_features, cat_features, num_features):
    res = []
    res += bin_features
    for cat_feature in cat_features:
        res += list(map(lambda x: cat_feature + '_' + str(x), range(cat_features[cat_feature])))
    res += num_features
    return res


def generate_cat_feature_counts(df, cat_features):
    return dict(zip(cat_features, list(map(lambda cat: df[cat].nunique(), cat_features))))
