""" Connection to  Elastic Search database and methods to load a csv file into that database """

import json
import csv
from elasticsearch import Elasticsearch



CREDENTIALS = "resources/credentials.json"


def ElasticSearchConnection():
    """Connect to ElasticSearch"""
    try:
        _USER, _PASSWORD, _CLOUD_ID = json.load(open(CREDENTIALS)).values()
        return Elasticsearch(cloud_id=_CLOUD_ID, http_auth=(_USER, _PASSWORD), timeout=60)
    except ConnectionError:
        print("Error connecting to ElasticSearch\n")
        raise
    except FileNotFoundError:
        print(f"File {CREDENTIALS} not found\n")
        raise


def loadCsv():
    """Load csv file into ElasticSearch"""
    pass


def getData():
    """ Query data from ElasticSearch """
    pass





if __name__ == '__main__':
    es = ElasticSearchConnection()
    print(es.ping())
