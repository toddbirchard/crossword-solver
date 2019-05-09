"""Read JSON from file into Python dictionary."""
import json


def read_json_data(json_file):
    """Load data from JSON file."""
    with open(json_file, 'r') as f:
        dataDict = json.load(f)
        return dataDict
