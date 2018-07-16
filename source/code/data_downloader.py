from tqdm import tqdm
import os
import subprocess
import logging
import json


class DataDownloader:

    def __init__(self, configuration_path):
        self.logger = logging.getLogger(DataDownloader.__name__)
        self.logger.setLevel(logging.INFO)
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        self.logger.addHandler(ch)
        self.logger.info('\nINITIALIZING...')
        configuration = json.load(open(configuration_path, 'r'))
        self.local_path = configuration['local_path']
        self.dataset = configuration['dataset']
        self.logger.info('INITIALIZATION HAS BEEN COMPLETED')

    def get_raw_data(self):
        if not os.path.exists(os.path.join(self.local_path, 'downloaded')):
            self.logger.info('ARCHIVE FILE HAS NOT BEEN DOWNLOADED YET')
            if not os.path.exists(self.local_path):
                self.logger.info('CREATE LOCAL DIRECTORY')
                os.mkdir(self.local_path)
            self.logger.info('START DOWNLOADING ARCHIVES')



            downloader_process_line = 'kaggle competitions download -c {} --path {}'
            bashCommand = downloader_process_line.format(self.dataset, self.local_path)
            output = subprocess.call([bashCommand], shell=True)

            open(os.path.join(self.local_path, 'downloaded'), 'a').close()



            self.logger.info('ARCHIVES DOWNLOADING HAS BEEN COMPLETED')
            # ==========================================================================================================
            if not os.path.exists(os.path.join(self.local_path, 'unzipped')):
                self.logger.info('ARCHIVE FILE HAS NOT BEEN UNZIPPED YET')
                self.logger.info('UNZIP ARCHIVE FILE')
                # TODO: unzipping
                # open(os.path.join(self.local_path, 'unzipped'), 'a').close()
                self.logger.info('ARCHIVE FILE HAS BEEN UNZIPPED')
            # ==========================================================================================================
        else:
            self.logger.info('ARCHIVE FILE HAS BEEN ALREADY DOWNLOADED')
            # ==========================================================================================================
            if not os.path.exists(os.path.join(self.local_path, 'unzipped')):
                self.logger.info('ARCHIVE FILE HAS NOT BEEN UNZIPPED YET')
                self.logger.info('UNZIP ARCHIVE FILE')
                # TODO: unzipping
                # open(os.path.join(self.local_path, 'unzipped'), 'a').close()
                self.logger.info('ARCHIVE FILE HAS BEEN UNZIPPED')
            # ==========================================================================================================
            else:
                self.logger.info('ARCHIVE FILE HAS BEEN ALREADY UNZIPPED')

    def extract_documents(self, docs_count_per_topic=0):
        files = [f for f in os.listdir(self.local_path) if os.path.isfile(os.path.join(self.local_path, f))]
        files = [f for f in files if '.txt' in f]
        topic_labels = dict(zip(list(map(lambda x: x[:-4], files)), range(len(files))))
        file_paths = [os.path.join(self.local_path, f) for f in files]
        labelled_documents = []
        labels = []
        for file_path in tqdm(file_paths, desc='Files reading and documents extraction'):
            with open(file_path, 'r', encoding='utf8', errors='ignore') as documents_source:
                lines = documents_source.readlines()
                lines = list(map(str.strip, lines))
                lines = list(filter(lambda line: 'From: ' not in line, lines))
                lines = list(filter(lambda line: 'Subject: ' not in line, lines))
                lines = list(filter(lambda line: 'document_id: ' not in line, lines))
                lines = list(filter(lambda line: 'Last-modified: ' not in line, lines))
                lines = list(filter(lambda line: 'Version: ' not in line, lines))
                lines = list(filter(lambda line: '@' not in line, lines))
                lines = list(filter(lambda line: len(line) > 0, lines))
                full_text = ' '.join(lines)
                label = file_path.split('/')[-1][:-4]
                documents = full_text.split('Newsgroup: {}'.format(label))
                if docs_count_per_topic > 0:
                    labelled_documents.extend(documents[0:docs_count_per_topic])
                    labels.extend([topic_labels[label]] * docs_count_per_topic)
                else:
                    labelled_documents.extend(documents)
                    labels.extend([topic_labels[label]] * len(documents))
        return labelled_documents, labels
