import re
import requests

url = "https://www.achrnews.com/directories/2937-hvacr-directory/listing/8472-ebac-industrial-products-inc-newport-news-va"
response = requests.get(url)
content = response.text
# print(content)

print(re.search(r'EB[^"]*',content)[0])
# company_name = re.search(r'<meta property="og:title" content="([^"]+)" />',content)
# print(company_name[1])

phone_number_pattern = r'\(\d{3}\) \d{3}-\d{4}'
phone_numbers = re.findall(phone_number_pattern, content)

for phone_number in phone_numbers:
    print(phone_number)

email = re.search(r'href="mailto:([^"]+)"', content)
if email:
    email_address = email.group(1)
    print('Email:',email_address)
