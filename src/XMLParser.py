import xml.etree.ElementTree as ET
from src.news import News


class XMLParser:

    def __init__(self, path):
        self.doc = ET.parse(path)
        self.root = self.doc.getroot()

    def parse(self):
        coco = []
        items = self.root.find('channel').findall('item')
        for child in items:
            new = News()
            new.title = child.find('title').text
            coco.append(new)
        return coco
