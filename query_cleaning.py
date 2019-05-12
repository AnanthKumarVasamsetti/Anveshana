import sys
import json
from pprint import pprint
import string
import data_cleaning as dc
#if len(sys.argv) > 1:
argument='{"query":"Kms api/services failing with 404 errorcode","Tag":"kms/engagement"}'
print(argument)
if isinstance(argument, str):
    query = json.loads(argument)
    tokened_query=dc.clean_data(query['query'])
    print(tokened_query)
