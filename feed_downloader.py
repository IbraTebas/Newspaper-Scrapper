import requests
import pandas as pd


def main():
    feed_el_pais = 'https://www.elpais.com.uy/rss/'
    feed_brecha = 'https://brecha.com.uy/feed/'
    feed_el_observador = "https://www.elobservador.com.uy/rss/elobservador.xml"
    feed_la_diaria = 'https://ladiaria.com.uy/feeds/articulos/'
    today = "{}-{}-{}".format(str(pd.to_datetime("today").date())[8:10], str(pd.to_datetime("today").date())[5:7],
                              str(pd.to_datetime("today").date())[0:4])
    now = str(pd.to_datetime("today").time())[0:5]
    response = requests.get(feed_el_pais)
    with open('./feeds/elpais/Elpais-{}-{}hs{}min.xml'.format(today, now[0:2], now[3:5]), 'wb') as file:
        file.write(response.content)
    response = requests.get(feed_brecha)
    with open('./feeds/brecha/Brecha-{}-{}hs{}min.xml'.format(today, now[0:2], now[3:5]), 'wb') as file:
        file.write(response.content)
    response = requests.get(feed_el_observador)
    with open('./feeds/elobservador/elobservador-{}-{}hs{}min.xml'.format(today, now[0:2], now[3:5]), 'wb') as file:
        file.write(response.content)
    response = requests.get(feed_la_diaria)
    with open('./feeds/ladiaria/ladiaria-{}-{}hs{}min.xml'.format(today, now[0:2], now[3:5]), 'wb') as file:
        file.write(response.content)


if __name__ == '__main__':
    main()
