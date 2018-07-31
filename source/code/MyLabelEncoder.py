from sklearn.base import TransformerMixin
from sklearn.preprocessing import LabelEncoder


class MyLabelEncoder(TransformerMixin):

    def __init__(self, *args, **kwargs):
        self.encoder = LabelEncoder()

    def fit(self, x, y=0):
        self.encoder.fit(x)
        return self

    def transform(self, x, y=0):
        return self.encoder.transform(x).reshape(-1, 1)
