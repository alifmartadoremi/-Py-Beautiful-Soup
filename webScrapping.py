__author__='Kvda'

from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import re


def scrapping_ori_script():
    url = "http://indeks.kompas.com/indeks/index/news"

    result = requests.get(url)
    scriptWeb = result.content
    yusup = BeautifulSoup(scriptWeb, 'lxml')

    linkPilihanSiUcup = []

    for linkKesukaanSiYusup in yusup.find_all("h3"):
        kabogohnaYusup = linkKesukaanSiYusup.find('a')
        linkPilihanSiUcup.append(kabogohnaYusup.attrs['href'])

    print(linkPilihanSiUcup)

def testing_scrapping_rapih():
    url = "http://indeks.kompas.com/indeks/index/news"

    result = requests.get(url)
    scriptWeb = result.content
    yusup = BeautifulSoup(scriptWeb, 'lxml')
    getLink = []
    getTitleReal = []

    for linkKesukaanSiYusup in yusup.find_all('div', attrs={'class':'article__list__ clearfix'}):
        getLin = linkKesukaanSiYusup.find('a')
        getJud = linkKesukaanSiYusup.find('img')
        getLink.append(linkKesukaanSiYusup.find('a', attrs='href'))
        getTitleReal.append(linkKesukaanSiYusup.find('img', attrs='alt'))
        #getLink.append(getLin.attrs['href'])
        #getTitleReal.append(getJud.attrs['alt'])
        print(getLink)
        #print(linkKesukaanSiYusup)


    linkPilihanSiUcup = []

def New_Thief():
    target = 'http://indeks.kompas.com/indeks/index/news'

    open_target = urlopen(target)
    save_target = open_target.read()
    open_target.close()

    filename = "KompasWeb.csv"
    f = open(filename,"w")
    headers = "Judul, Genre, Pubdate, Link\n"
    f.write(headers)

    convert_to_html = BeautifulSoup(save_target, "html.parser")
    # get_news = convert_to_html.findAll("div",{"class":"article__list clearfix"})
    # get_img = convert_to_html.findAll("div",{"class":"article__list__asset clearfix"})
    # get_title= convert_to_html.findAll("div",{"class":"article__list__title"})
    # get_info = convert_to_html.findAll("div",{"class":"article__list__info"})

    get_news = convert_to_html.findAll("div", {"class": "article__list clearfix"})
    # get_img = get_news.find("div", {"class": "article__list__asset clearfix"})
    # get_title = get_news.findAll("div", {"class": "article__list__title"})
    # get_info = get_news.findAll("div", {"class": "article__list__info"})
    # tes = get_title[0]
    # tis = tes.h3.a.string
    # bre = tes.h3.a["href"]
    # bruh = get_news[0]
    # bruuh = bruh.find("div",{"class":"article__list__title"})

    for loop in get_news:

        get_img = loop.find("div", {"class": "article__list__asset"})
        get_title = loop.find("div", {"class": "article__list__title"})
        get_genre = loop.find("div", {"class": "article__subtitle article__subtitle--inline"})
        get_pubdate = loop.find("div", {"class": "article__date"})

        genre = get_genre.string
        pubdate = get_pubdate.string
        title = get_title.a.string
        link = get_title.a["href"]
        img = get_img.a.img["" \
                            "src"]

        execute_link = urlopen(link)
        save_link = execute_link.read()
        execute_link.close()

        sup = BeautifulSoup(save_link, "html.parser")


        get_konten = sup.find("div",{"class":"read__content"})
        # cleanse =re.sub(r'<strong>Baca\sjuga\:.*?</strong>','',str(get_konten))
        # bersih = cleanse.text
        # print(bersih)

        cleansing = BeautifulSoup(re.sub(r'<strong>Baca\sjuga\:.*?</strong>','',str(get_konten)),"html.parser")
        konten = cleansing.text
        #print(konten)
        # print(BeautifulSoup(re.sub(r'<strong>Baca\sjuga\:.*?</strong>','',str(get_konten))),"html.parser")
        print("Judul : "+title+"\nGenre : "+genre+"\nPubdate : "+pubdate+"\nLink : "+link+"\nImage : "+img+"\nKonten : \n"+konten+"\n----------------------")
        f.write(title.replace(',','')+","+genre+","+pubdate+","+link+"\n")
    print("Copyright © 2019 Kvda All Rights Reserved")




if __name__ == "__main__" :
    New_Thief()
    # scrapping_ori_script()
    #testing_scrapping_rapih()