from bs4 import BeautifulSoup
import requests

keyword = 'Bitcoin'
post_num = 10
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    }

def get_bbc(keyword, post_num):
    data = []

    for x in range(post_num):
        page = x + 1
        url = 'https://www.bbc.co.uk/search?'
        params = {
            'q': keyword,
            'page': page
        }
        res = requests.get(url, params=params, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')

        contents = soup.find_all(attrs={'class': 'ssrcss-11rb3jo-Promo ett16tt0'})
        count = len(contents)
        for x in range(count):
            title = contents[x].find(attrs={'class': 'ssrcss-atl1po-PromoLink e1f5wbog0'})
            img_url = contents[x].find(attrs={'class': 'ssrcss-1drmwog-Image ee0ct7c0'})
            url = contents[x].find(attrs={'class': 'ssrcss-atl1po-PromoLink e1f5wbog0'})
            article = get_article(url)
            content = {
                'title': title.text,
                'img_url': img_url['src'],
                'article': article['href']
            }
            data.append(content)

    return data


def get_article(url):
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    paragraph = []
    articles = soup.find_all(attrs={'class': 'ssrcss-1q0x1qg-Paragraph eq5iqo00'})
    count = len(articles)
    count = count - 4
    # Collect Data
    for x in range(count):
        p = articles[x].text
        paragraph.append(p)
    # Make Article
    row = ''
    for p in paragraph:
        row = row + p + ' <br><br> '

    return row


print(get_bbc(keyword, post_num))