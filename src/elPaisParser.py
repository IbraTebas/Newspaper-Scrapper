import xml.etree.ElementTree as ET
from src.news import News

dict_month = {'Jan': "01", 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08',
              'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dic': '12'}


def format_date(text):
    day = text[0:2]
    month = dict_month[text[3:6]]
    year = text[7:12]
    result = '{}-{}-{}'.format(day, month, year)
    return result


def remove_unicode(text):
    return text.replace("&nbsp;", "").replace('&gt', "").replace("<br>", "").replace("<i>", "")


def parser_text(tag, element):
    search = element.find(tag)
    if search is not None:
        return remove_unicode(search.text)
    return ''


class ElPaisParser:

    def __init__(self, path):
        self.doc = ET.parse(path)
        self.root = self.doc.getroot()

    def parse(self):
        parsing = []
        items = self.root.find('channel').findall('item')
        for child in items:
            new = News()
            new.title = parser_text('title', child)
            new.category = parser_text('category', child)
            new.description = parser_text('description', child)
            new.day = format_date(parser_text('pubDate', child)[5:16])
            new.time = parser_text('pubDate', child)[17:22]
            new.link = parser_text('link', child)
            new.author = parser_text('author', child)
            new.subtitle = parser_text('subtitle', child).capitalize()
            parsing.append(new)
        return parsing
