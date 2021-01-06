from src.XMLParser import XMLParser

def main():
    print('starting class example usage ...')
    parser = XMLParser('./feeds/elpais/Elpais-03-01-2021-22hs17min.xml')
    news = parser.parse()
    for n in news:
        print(n.title)
    print('process finished')


if __name__ == '__main__':
    main()
