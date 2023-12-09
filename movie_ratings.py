import requests
from bs4 import BeautifulSoup
import re

urls = ['https://www.123telugu.com/reviews/keedaa-cola-telugu-movie-review.html', 'https://timesofindia.indiatimes.com/entertainment/telugu/movie-reviews/keedaa-cola/movie-review/104938839.cms']
for url in urls:
    response = requests.get(url)
    page_source = response.text

    jsoup = BeautifulSoup(page_source)
    jsoup = jsoup.find("body")
    text = jsoup.text.replace(' ','')

    title = re.search(r'\/([a-zA-Z-]*)-telugu', url)
    if title:
        print(title.group(1))

    rating = re.search('\d\.?\d?\d?/(5|10)\.?\d?', text)
    # rating = re.search(r'\d[.\d]*/\d[.0]*', text)
    if rating:
        rating = rating.group(0)
    print(rating)
