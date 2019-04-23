import yaml
import pandas as pd


def open_yml(path):
    """Return a dict form a yml file.

    :param path: path to a yml file
    :type path: str
    :return: dictionnary corresponding at yml file
    :rtype: dict
    """
    returned_dic = {}
    with open(path, 'r') as stream:
        returned_dic = yaml.load(stream)
    return returned_dic


def create_yml(path, data):
    with open(path, 'w') as outfile:
        yaml.dump(data, outfile, default_flow_style=False)
