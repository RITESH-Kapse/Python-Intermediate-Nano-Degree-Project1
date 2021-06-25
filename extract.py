"""Extract data on near-Earth objects and close approaches\
from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments
provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing
    data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    with open(neo_csv_path, 'r') as infile:
        reader = csv.DictReader(infile)
        objects_neo = []

        for val in reader:
            objects_neo.append(
                               NearEarthObject(
                                   pdes=val['pdes'],
                                   name=val['name'], pha=val['pha'],
                                   diameter=val['diameter']
                                               )
                               )

    return objects_neo


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing
    data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    with open(cad_json_path, 'r') as infile:
        contents = json.load(infile)
        data = contents['data']
        objects_approach = []

        for val in data:
            objects_approach.append(
                                    CloseApproach(
                                        des=val[0],
                                        cd=val[3],
                                        dist=val[4],
                                        v_rel=val[7]
                                    ))

    return objects_approach