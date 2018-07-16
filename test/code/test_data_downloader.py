import unittest
from source.code.data_downloader import DataDownloader
from collections import Counter


class TestDataDownloader(unittest.TestCase):

    def setUp(self):
        self.data_downloader = DataDownloader(configuration_path='../../data/dataset_description.json')

    def test_get_raw_data(self):
        self.data_downloader.get_raw_data()

    def test_extract_documents(self):
        documents, labels = self.data_downloader.extract_documents()
        self.assertEqual(len(documents), len(labels), 'All documents should have a label!!!')
        self.assertEqual(20, len(Counter(labels).keys()), 'The topics count should be equal 20!!!')


if __name__ == '__main__':
    unittest.main()
