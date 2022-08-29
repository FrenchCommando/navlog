# builds the json data file from the input folder
# One file per person
# Select file using different values in the main

import os
import logging
import json
from utils.logger import process_logger
from input_data.parse_data import read_data

logger = logging.getLogger('input_data')
process_logger(logger, file_name="json_data")


def build_json(folder):
    data = read_data(folder=folder)
    with open(os.path.join(folder, 'input.json'), 'w+') as f:
        json.dump(data, f, indent=4)
        logger.debug("json dumped %s", f.name)


def build_input(folder):
    input_full_folder = os.path.join(os.getcwd(), "input_data", folder)
    build_json(input_full_folder)


def main():
    build_input(folder="stuff")


if __name__ == "__main__":
    main()
