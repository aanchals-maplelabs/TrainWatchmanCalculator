import xmltodict
import json

with open('report.xml') as in_file:
    xml = in_file.read()
    with open('json_report.json', 'w') as out_file:
        json.dump(xmltodict.parse(xml), out_file)