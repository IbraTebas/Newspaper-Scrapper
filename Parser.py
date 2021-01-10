import xml.etree.ElementTree as ET

dict_month = {'Jan': "01", 'Feb':'02', 'Mar':'03','Apr': '04','May':'05', 'Jun':'06', 'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dic':'12'}
def format_date_elpais(date_elpais):
    day=date_elpais[0:2]
    month=dict_month[date_elpais[3:6]]
    year= date_elpais[7:12]
    result='{}-{}-{}'.format(day, month, year)
    return result


class News:

    def __init__(self):
        self.day = ''
        self.time = ''
        self.title = ''
        self.subtitle = ''
        self.category = ''
        self.description = ''
        self.author = ''
        self.link = ''


class XMLParser:

    def __init__(self, path):
        self.doc = ET.parse(path)
        self.root = self.doc.getroot()

    def remove_unicode(self, text):
        return text.replace("&nbsp;", "").replace('&gt', "").replace("<br>", "")


    def parser_text(self, tag, element):
        search = element.find(tag)
        if search is not None:
            return self.remove_unicode(search.text)
        return ''


    def parse(self):
        parsing = []
        items = self.root.find('channel').findall('item')
        for child in items:
            new = News()
            # Title section parser
            new.title = self.parser_text('title', child)
            new.category = self.parser_text('category', child)
            new.description = self.parser_text('description', child)
            new.day = self.parser_text('pubDate', child)[5:16]
            new.time = self.parser_text('pubDate', child)[17:22]
            new.day = format_date_elpais(new.day)
            new.link = self.parser_text('link', child)
            new.author = self.parser_text('author', child)
            new.subtitle = self.parser_text('subtitle', child).capitalize()
            parsing.append(new)
        return parsing


News=XMLParser('Elpais-03-01-2021-22hs45min.xml').parse()

import pandas as pd
pd.set_option('max_colwidth', None)
df=pd.DataFrame([vars(s) for s in News])
df

