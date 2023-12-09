import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.imdb.com/chart/moviemeter/'

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'

}

response = requests.get(url,headers= header)
# print(response)
# print(response.content)

page_source = response.content

jsoup =BeautifulSoup(page_source)

body = jsoup.find('ul',attrs={'class': 'ipc-metadata-list ipc-metadata-list--dividers-between sc-3f13560f-0 sTTRj compact-list-view ipc-metadata-list--base'})

result = body.find_all('li',attrs={'class':'ipc-metadata-list-summary-item sc-59b6048d-0 jemTre cli-parent'})
# print(result)
final_result = []
for li in result:
    dummy = dict()
    h3 = li.find('h3',attrs={'class':'ipc-title__text'})
    span = li.find('span',attrs = {'class':'sc-4dcdad14-8 cvucyi cli-title-metadata-item'})
    time_span = li.find_all('span', attrs = {'class':'sc-4dcdad14-8 cvucyi cli-title-metadata-item'})
    # print(time_span)
    rating = li.find('span',attrs = {'class':'ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating'})
    # print(rating)
    voting = li.find('span',attrs = {'class':'ipc-rating-star--voteCount'})
    # print(voting)
    if len(time_span) >= 3:
        time = time_span[1].get_text()
        age_limit = time_span[2].get_text()

    title = h3.text
    year = span.text
    ratings = rating['aria-label'] if rating else None
    votes = voting.text.replace('\xa0', '').strip('()') if voting else None

    dummy['Movie Name'] = title
    dummy['Year'] = year
    dummy['Duration'] = time
    dummy ['Age Limit'] = age_limit
    dummy['Rating'] = ratings
    dummy['Votes'] = votes
    final_result.append(dummy)

print(final_result)

df = pd.DataFrame(final_result)
# print(df)
# df.to_csv('D:\\$PYTHON\\popular movies imdb.csv', index=False)
