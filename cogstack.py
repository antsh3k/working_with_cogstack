import getpass
import elasticsearch
import elasticsearch.helpers
import pandas as pd
from typing import Dict, List
from tqdm.notebook import tqdm

import warnings
warnings.filterwarnings("ignore")

from credentials import *


class CogStack(object):
    def __init__(self, hosts: List, username: str=None, password: str=None,
                 api_username: str=None, api_password: str=None, api=False):
        """

        :param hosts:
        :param username:
        :param password:
        :param api_username:
        :param api_password:
        :param api:
        """
        if api:
            api_username, api_password = self._check_api_auth_details(api_username, api_password)
            self.elastic = elasticsearch.Elasticsearch(hosts=hosts,
                                                       http_auth=(api_username, api_password),
                                                       verify_certs=False)
        else:
            username, password = self._check_auth_details(username, password)
            self.elastic = elasticsearch.Elasticsearch(hosts=hosts,
                                                       basic_auth=(username, password),
                                                       verify_certs=False)

    def _check_api_auth_details(self, api_username=None, api_password=None):
        if api_username is None:
            api_username = input("API Username: ")
        if api_password is None:
            api_password = getpass.getpass("API Password: ")
        return api_username, api_password

    def _check_auth_details(self, username=None, password=None):
        if username is None:
            username = input("Username: ")
        if password is None:
            password = getpass.getpass("Password: ")
        return username, password

    def get_docs_generator(self, query: Dict, index: List, es_gen_size: int = 800, request_timeout: int = 300):
        """

        :param query: search query
        :param index: List of ES indices to search
        :param es_gen_size:
        :param request_timeout:
        :return: search generator object
        """
        docs_generator = elasticsearch.helpers.scan(self.elastic,
                                                    query=query,
                                                    index=index,
                                                    size=es_gen_size,
                                                    request_timeout=request_timeout)
        return docs_generator


def cogstack2df(cogstack_search_gen, column_headers=None):
    """
    Returns DataFrame from a CogStack search

    :param cogstack_search_gen: CogStack output generator object
    :param column_headers: specify column headers
    :return: DataFrame
    """
    results = [column_headers]
    for i, doc in enumerate(cogstack_search_gen):
        if column_headers is None:
            column_headers = ['id'] + list(doc['_source'].keys())
            results = [column_headers]
        result = []
        for col in column_headers:
            if col == 'id':
                result.append(doc['_id'])
            else:
                result.append(doc['_source'].get(col, ''))
        results.append(result)
    df_results = pd.DataFrame(results[1:], columns=results[0])
    return df_results


