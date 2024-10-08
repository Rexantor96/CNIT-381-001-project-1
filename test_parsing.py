import pytest
from parse_data import *

def test_parseXML():
    result = parseXML('parse.xml', 'edit-config', 'interface')
    assert result == 'TenGigE0/0/0/0'
    result = parseXML('parse.xml', 'edit-config', 'subinterfaces')
    assert result == '2'

def test_parseJSON():
    result = parseJSON("parse.json", 'name')
    assert result == 'Adeel Solangi'
    result = parseJSON("parse.json", 'id')
    assert result == 'V59OF92YF627HFY0'

def test_parseYAML():
    result = parseYAML("parse.json", 'name')
    assert result == 'Adeel Solangi'
    result = parseYAML("parse.json", 'id')
    assert result == 'V59OF92YF627HFY0'
