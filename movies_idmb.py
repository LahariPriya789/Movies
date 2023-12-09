import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.imdb.com/find/?q=telugu&ref_=nv_sr_sm'
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=header)

# print(response.content)
page_source = response.content



#----------------------------------------Bs4-------------------------------------------------------------

jsoup = BeautifulSoup(page_source)

body = jsoup.find('ul', attrs={'class':'ipc-metadata-list ipc-metadata-list--dividers-after sc-17bafbdb-3 gAWnDM ipc-metadata-list--base'})
# print(jsoup)
# print(body)
result = body.find_all('li', attrs={'class':'ipc-metadata-list-summary-item ipc-metadata-list-summary-item--click find-result-item find-title-result'})
# print(result)
finla_result = []
for li in result:
    dummy = dict()
    # print(li)
    a = li.find('a', attrs={'class':'ipc-metadata-list-summary-item__t'})
    # span = li.find('span',attrs={'class':'ipc-metadata-list-summary-item__li'})
    span = li.find_all('span',attrs={'class':'ipc-metadata-list-summary-item__li'})
    # print(actor_span)
    name = a.text
    link = a['href']
    year = span[0].text

    actor = span[-1].get_text()

    # print('Name: ', name)
    # print('Link: ', link)
    dummy['Movie Name'] = name
    dummy['Link'] = link
    dummy['Year'] = year
    dummy['Actor'] = actor
    finla_result.append(dummy)
    # break
print(finla_result)
df = pd.DataFrame(finla_result)

def remove(x):
    return x.replace('–','')

df['Year'] = df['Year'].apply(remove)
# print(df['Year'])
print(df)
