#!/usr/bin/env python3
'''
Created: 08.08.2019

@author: LK
'''

import PyTrinamic
import xml.etree.ElementTree as ET

class XMLHandler(object):
    def __init__(self, file):
        self._tree = ET.parse(file)
        self._root = self._tree.getroot()
