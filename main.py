from src.elPaisParser import ElPaisParser
import pandas as pd


def main():
    path_file = './feeds/elpais/Elpais-08-01-2021-16hs59min.xml'
    parser = ElPaisParser(path_file)
    news = parser.parse()
    bulk_to_pandas(news)


def bulk_to_pandas(news):
    df = pd.DataFrame([vars(s) for s in news])
    return df


if __name__ == '__main__':
    main()
