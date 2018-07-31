import unittest
from source.code.MyLabelEncoder import MyLabelEncoder
import pandas as pd


class TestMyLabelEncoder(unittest.TestCase):

    def setUp(self):
        self.encoder = MyLabelEncoder()

    def test_label_encoding_case_1(self):
        df = pd.DataFrame({'cat': ['a', 'b', 'c', 'd', 'e']})
        df_encoded = self.encoder.fit_transform(df)
        self.assertEquals(5, df_encoded.shape[0])


if __name__ == '__main__':
    unittest.main()
