import requests
from bs4 import BeautifulSoup

def get_article_content(url):

    response = requests.get(url)

    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.title.string
        paragraphs = soup.find_all(attrs={'data-component-name':'p'})
        content = ''

        paragraphs = soup.find_all("p")

        for paragraph in paragraphs:
            print(paragraph.text)
            print("-" * 20)  

        return title, content
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None, None

article_url = 'https://www.nytimes.com/2020/09/02/opinion/remote-learning-coronavirus.html'

title, content = get_article_content(article_url)
print('-'*30)
if(title != None and content != None): 
    print(title)
    print(content)
