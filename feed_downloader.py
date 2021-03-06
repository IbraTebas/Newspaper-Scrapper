import requests
import pandas as pd


def main():
    print('start feed downloading ...')
    feed_el_pais = 'https://www.elpais.com.uy/rss/'
    feed_brecha = 'https://brecha.com.uy/feed/'
    feed_el_observador = "https://www.elobservador.com.uy/rss/elobservador.xml"
    feed_la_diaria = 'https://ladiaria.com.uy/feeds/articulos/'
    feed_mvd_com_destacadas = 'https://www.montevideo.com.uy/anxml.aspx?58'
    feed_mvd_com_news = 'https://www.montevideo.com.uy/anxml.aspx?59'
    feed_mvd_com_opinion = 'https://www.montevideo.com.uy/anxml.aspx?1303'
    feed_busqueda = 'https://www.busqueda.com.uy/anxml.aspx?13'
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
    response = requests.get(feed_mvd_com_news)
    with open('./feeds/mvdcom/mvd_com_news-{}-{}hs{}min.xml'.format(today, now[0:2], now[3:5]), 'wb') as file:
        file.write(response.content)
    response = requests.get(feed_mvd_com_destacadas)
    with open('./feeds/mvdcom/mvd_com_destacadas-{}-{}hs{}min.xml'.format(today, now[0:2], now[3:5]), 'wb') as file:
        file.write(response.content)
    response = requests.get(feed_mvd_com_opinion)
    with open('./feeds/mvdcom/mvd_com_opinion-{}-{}hs{}min.xml'.format(today, now[0:2], now[3:5]), 'wb') as file:
        file.write(response.content)
    response = requests.get(feed_busqueda)
    with open('./feeds/busqueda/busqueda-{}-{}hs{}min.xml'.format(today, now[0:2], now[3:5]), 'wb') as file:
        file.write(response.content)

    print('file downloaded successfully')


if __name__ == '__main__':
    main()
