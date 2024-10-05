import xml.etree.ElementTree as tree
import re
import json
import yaml

def parseXML(file, tag, value):
    tag = "{}" + tag
    value = "{}" + value
    xmlFile = tree.parse(file)
    root = xmlFile.getroot()
    xml = re.match('{.*}', root.tag).group(0)
    item = root.find(tag.format(xml))
    result = item.find(value.format(xml))
    return "{}".format(result.text)

def parseJSON(file, key):
    with open(file, "r") as jsonFile:
        data = json.load(jsonFile)
    result = "{}".format(data['name'])
    return result

def parseYAML(file, key):
    with open(file, "r") as yamlFile:
        data = yaml.safe_load(yamlFile)
    result = "{}".format(data['name'])
    return result

print(parseXML("parse.xml", "bk112", "author"))
#print(parseJSON("parse.json", 'Abbrev'))
#print(parseYAML("parse.yaml", 'Abbrev'))

#https://microsoftedge.github.io/Demos/json-dummy-data/