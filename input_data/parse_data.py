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

    for f in glob.glob(os.path.join(folder, "*")):
        name = os.path.basename(f)
        if name == input_json_name:
            continue
        data_json = parse_json(f)
        data['json'].append(data_json)
    return data
