import requests
from requests.auth import HTTPBasicAuth
import es_config
import json


bauth = HTTPBasicAuth(es_config.es_user, es_config.es_password)

def insert_into_es(each_doc, index):
#     print(each_doc, index, es_config.es_url)
    insert_request = requests.post(url="{}/{}/_doc/".format(es_config.es_url,index),
                                       auth=bauth,
                                       data=json.dumps(each_doc),
                                       headers=es_config.es_request_headers).json()
#     print(insert_request)
