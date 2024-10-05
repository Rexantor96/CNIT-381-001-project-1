import xml.etree.ElementTree as tree
import re
import json

def parseXML(file, tag, value):
    tag = "{}" + tag
    value = "{}" + value
    xmlFile = tree.parse(file)
    root = xmlFile.getroot()
    xml = re.match('{.*}', root.tag)
    item = root.find(tag.format(xml))
    result = item.find(value.format(xml))
    return "{}".format(result.text)

def parseJSON(file, key):
    with open(file, "r") as jsonFile:
        data = json.load(jsonFile)
    result = "{}".format(data['name'])
    return result

#print(parseXML("parse.xml", "bk112", "author"))
#print(parseJSON("parse.json", 'Abbrev'))

#https://microsoftedge.github.io/Demos/json-dummy-data/
#https://learn.microsoft.com/en-us/previous-versions/windows/desktop/ms762271(v=vs.85)