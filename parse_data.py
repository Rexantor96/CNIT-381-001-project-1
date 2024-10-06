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
    result = "{}".format(data[key])
    return result

def parseYAML(file, key):
    with open(file, "r") as yamlFile:
        data = yaml.safe_load(yamlFile)
    result = "{}".format(data[key])
    return result

print(parseXML("/home/willw/test.xml", 'edit-config', 'test-option'))
#print(parseJSON("parse.json", 'name'))
#print(parseYAML("parse.yaml", 'name'))

#https://microsoftedge.github.io/Demos/json-dummy-data/