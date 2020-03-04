import json
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['reports']
collection_currency = db['pytest_report']

with open('json_report.json') as f:
    file_data = json.load(f)

# if pymongo >= 3.0 use insert_one() for inserting one document
collection_currency.insert_one(file_data)

client.close()