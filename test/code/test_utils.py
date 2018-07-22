import unittest
from source.code.utils import generate_features_names


class TestUtils(unittest.TestCase):

    def test_generate_features_names(self):
        num_features = ['with', 'height', 'age']
        bin_features = ['gender']
        cat_features = {'marital_status': 5, 'home_type': 3}
        res = generate_features_names(bin_features, cat_features, num_features)
        self.assertEqual(12, len(res), 'Something is wrong!!!')
