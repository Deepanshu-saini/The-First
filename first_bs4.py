import requests
from bs4 import BeautifulSoup
def extract_news(url):
    websites=[]
    headers= {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}
    print('Extracting Hacker News Stories...')
    cnt = ''
    cnt +=('<b>HN Top Stories:</b>\n'+'<br>'+'-'*50+'<br>')
    response = requests.get(url,headers=headers)
    content = response.content
    print(content)
    contents = BeautifulSoup(content, 'html.parser')
    panels_blocks = contents.find_all('div', class_='row panel panel-default rowP')
        
    for block in panels_blocks:
        links = block.find_all('a', class_ = 'btn btn-link btn-lg')
        website_name = links[0].text.split('\n')[1]
        website_url = website_name
        if len(links)>1:
            website_url = links[1].get('href')
        websites.append(website_url)
    return websites
cnt = extract_news('https://sitelike.org/similar/gmail.com/')
print(cnt)