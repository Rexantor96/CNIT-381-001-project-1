import xml.etree.ElementTree as tree
import re

def parseXML(file, tag, value):
    tag = "{}" + tag
    value = "{}" + value
    xmlFile = tree.parse(file)
    root = xmlFile.getroot()
    xml = re.match('{.*}', root.tag)
    item = root.find(tag.format(xml))
    result = item.find(value.format(xml))
    return "{}".format(result.text)

print(parseXML("parse.xml", "bk112", "author"))
