import bs4
import requests

def get_price(product_url):
    res = requests.get(product_url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems  = soup.select('#details-page > section > div.details-book-main-info-wrapper > div > div.col.details-book-main-info.align-self-center > div.details-book-main-info__content > p.details-book-info__content-book-price')
    price = elems[0].text.strip().replace(' ', '').replace('\n', '')
    return price[:6]

price = get_price('https://www.rokomari.com/book/180038/charpoka--the-battle-of-mahendrapur-')
print('The price is ' + price)