import unittest
from sklearn.pipeline import Pipeline
from sklearn.pipeline import FeatureUnion
from source.code.utils import generate_encoded_pipeline
import pandas as pd


class TestPipeline(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            'cat_1': ['a', 'b', 'c', 'd', 'e'],
            'cat_2': ['1', '2', '3', '4', '5']
        })

    def test_label_encoding_case_1(self):
        self.pipeline = Pipeline([
            ('union', FeatureUnion(
                list(map(generate_encoded_pipeline, ['cat_1', 'cat_2']))
            ))
        ])
        df_trans = self.pipeline.fit_transform(self.df)
        self.assertEquals(5, df_trans.shape[0])


if __name__ == '__main__':
    unittest.main()
