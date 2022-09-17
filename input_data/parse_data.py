import os
import glob
import json
import logging
from utils.forms_constants import input_json_name


logger = logging.getLogger('input_data')


def parse_json(path):
    # parsing json file
    with open(path, "r") as f:
        data_json = json.load(f)
    return data_json


def read_data(folder):
    data = dict(json=[])
    with open(os.path.join(folder, "navlog_list.txt"), "r") as f:
        file_list = f.readlines()
    for file in file_list:
        data_json = parse_json(os.path.join(folder, file.strip()))
        data['json'].append(data_json)
    return data
