from bs4 import BeautifulSoup
from selenium import webdriver
import csv


def get_url(search_term):
    template = 'https://www.amazon.in/s?i=electronics&bbn=976419031&rh=n%3A976419031%2Cp_89%3Arealme&dc'
    url_page = template.format(search_term)
    url_page += '&page{}'
    return url_page


def extract_record(item):
    atag = item.h2.a
    description = atag.text.strip()
    url = 'https://www.amazon.com' + atag.get('href')
    try:
        price_parent = item.find('span', 'a-price')
        price = price_parent = item.find('span', 'a-offscreen').text
        price = price[1:]
        price = price.replace(',','')
        float(price)
    except AttributeError:
        return

    try:
        rating = item.i.text
        rating = float(rating[0:3])
        review_count = item.find('span', {'class': 'a-size-base'}).text
    except AttributeError:
        rating = ''
        review_count = ''

    result = (description, price, rating, review_count, url)
    return result

def main(search_term):
    # Starting up the webdriver
    driver = webdriver.Chrome(executable_path=r'C:/Users/Rejoice/chromedriver_win32/chromedriver.exe')

    #url = 'https://www.amazon.in/s?bbn=976419031&rh=n%3A976419031%2Cp_89%3Arealme&dc&qid=1624216249&rnid=3837712031&ref=lp_976420031_nr_p_89_3'
    #driver.get(url)

    records = []
    url=get_url(search_term)

    for page in range(7):
        driver.get(url.format(page))

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        results = soup.find_all('div', {'data-component-type': 's-search-result'})

        for item in results:
            record = extract_record(item)
            if record:
                records.append(extract_record(item))

    driver.close()

    with open('results.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Description','Price','Rating (out of 5)','ReviewCount','url'])
        writer.writerows(records)

    #return search_term
