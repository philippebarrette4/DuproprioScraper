import xlsxwriter
import requests
from bs4 import BeautifulSoup

workbook = xlsxwriter.Workbook('duproprio.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write('A1', 'City')
worksheet.write('B1', 'Price')

i = 2

for page in range(1,30):

    URL = f'https://duproprio.com/fr/lanaudiere/maison-a-vendre?pageNumber={page}'.format(page)

    headers = {
        "User-Agent":
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:85.0) Gecko/20100101 Firefox/85.0'
    }

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    test = soup.findAll("div", class_="search-results-listings-list__item-bottom-container")


    for t in test:
        if(t.find("div", class_="search-results-listings-list__item-description__price")):
            p = t.find("div", class_="search-results-listings-list__item-description__price").text
            p = "".join((str(p[:-2]).strip()).split())
            c = t.find("h3", class_="search-results-listings-list__item-description__item search-results-listings-list__item-description__city").text
            c = str(c).strip()

            Col1 = "A" + str(i)
            print(Col1)
            Col2 = "B" + str(i)
            print(Col2)

            worksheet.write(Col1, c)
            worksheet.write(Col2, p)
        else:
            i = i-1

        i = i+1

workbook.close()
