import pandas as pd
pd.set_option('max_colwidth', None)
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

    def parse(self):
        parsing = []
        items = self.root.find('channel').findall('item')
        for child in items:
            new = News()
            # Title section parser
            new.title = child.find('title').text
            new.category = child.find('category').text

            # Description section parser
            if child.find('description') is None:
                pass
            else:
                new.description = child.find('description').text.replace("&nbsp;", "")
                new.description = new.description.replace("&gt", "")
                new.description = new.description.replace("<br>", "")
                # Day and time section, converting at the same format of the file name
            new.day = child.find('pubDate').text[5:16]
            new.day = format_date_elpais(new.day)
            new.time = child.find('pubDate').text[17:22]
            new.link = child.find('link').text
            # Author section
            if child.find('author') is None:
                pass
            else:
                new.author = child.find('author').text
                # Subtitle section
            if child.find('subtitle') is None:
                pass
            else:
                new.subtitle = child.find('subtitle').text
                new.subtitle = new.subtitle.capitalize()
            parsing.append(new)
        return parsing

# def main():
#     print('starting class example usage ...')
#     parser = XMLParser('Elpais-03-01-2021-22hs45min.xml')
#     news = parser.parse()           #si le aplico list a news tengo el objeto buscado
#     for n in news:
#         print(n.title)
#     print('process finished')


# if __name__ == '__main__':
#     main()

# Sun, 03 Jan 2021 07:00:00
#   lst=['title', 'description', 'pubDate', 'link', 'subtitle', 'category','categorySlug', 'parentCategorySlug', 'articleSlug', 'author', 'imageCaption']

News=XMLParser('Elpais-03-01-2021-22hs45min.xml').parse()

df = pd.DataFrame([t.__dict__ for t in News ])        ###linea fundamental, esto convierte los objetos de la clase (es decir las noticias) y las vierte en una pandas dataframe.

df2=pd.DataFrame([vars(s) for s in News])              ###linea fundamental, esto convierte los objetos de la clase (es decir las noticias) y las vierte en una pandas dataframe variacion mas conservadora parece en terminso quer toma todo

df                                          ###se podria hacer lo siguiente para quedarse con las columnas que quieras: *****pd.DataFrame([vars(s) for s in signals], columns=['x', 'y'])***

df