import pytest
from parse_data import *

def test_parseXML():
    result = parseXML('parse.xml', 'edit-config', 'test-option')
    assert result == 'set'
    result = parseXML('parse.xml', 'edit-config', 'default-operation')
    assert result == 'merge'

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
