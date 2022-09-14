import json
from os import path
from glob import glob

from .collecting_formatter import CollectedFeature


def load_feature_file(feature_path):
    if not path.exists(feature_path):
        print('Unable to find feature file\n')
        exit(2)

    with open(feature_path, 'rt') as file:
        return CollectedFeature.from_json(json.load(file))


def load_all_feature_files_in_directory(featurespath):
    files = glob(path.join(featurespath, '*.json'))

    features = []
    for file in files:
        feature = load_feature_file(file)
        features.append(feature)

    return features
