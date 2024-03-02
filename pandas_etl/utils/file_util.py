import logging

import yaml


def load_yml(file_path):
    with open(file_path, 'r') as f:
        try:
            data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            logging.error(e)

    return data
