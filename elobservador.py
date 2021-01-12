from src.elObservadorParser import *
import pandas as pd


def main():
    path_file = './feeds/elobservador-06-01-2021-11hs01min.xml'
    parser = elObservadorParser(path_file)
    news = parser.parse()
    bulk_to_pandas(news)


def bulk_to_pandas(news):
    df = pd.DataFrame([vars(s) for s in news])
    return df


df=bulk_to_pandas(elObservadorParser('./feeds/elobservador/elobservador-06-01-2021-11hs01min.xml').parse())