from src.XML_Parser import *
import pandas as pd
pd.set_option('max_colwidth', None)


def main(path_file):
    parser = XMLParser(path_file)
    list_news_file = parser.parse()
    return list_news_file

def bulk_to_pandas(path_file):
    list_news_file = main(path_file)
    df = pd.DataFrame([vars(s) for s in  list_news_file])    
    return df




df=bulk_to_pandas('./feeds/elpais/Elpais-08-01-2021-16hs59min.xml')




















#df = pd.DataFrame([t.__dict__ for t in  list_news_file ]) can be used instead of the below.
#df=pd.DataFrame([vars(s) for s in  list_news_file]) #pd.DataFrame([vars(s) for s in  list_news_file], columns=['x', 'y']) would take only x and y for the pandas df.

#df


#if __name__ == '__main__':
 #   main('./feeds/elpais/Elpais-03-01-2021-22hs17min.xml')
 