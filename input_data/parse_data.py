import os
import glob
from collections import defaultdict
import xml.etree.ElementTree as eTree
import logging


logger = logging.getLogger('input_data')


def parse_xml(path, print_tag=False):
    # parsing xml file
    tree = eTree.parse(path)
    root = tree.getroot()

    for u in root:
        if print_tag:
            print(u)
            for t in u:
                print(t.tag, t.text)

    return root


def read_data(folder):
    data = defaultdict(list)

    for f in glob.glob(os.path.join(folder, "*")):
        name = os.path.basename(f)
        name_sub, extension = name.split(".")
        if extension == 'json':
            continue
        data_xml = parse_xml(f)
        data['xml'].append(data_xml)
    return data
