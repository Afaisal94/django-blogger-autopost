import requests


def get_foxnews(keyword, post_num):
    data = []
    url = 'https://api.foxnews.com/search/web?q=Bitcoin+-filetype:amp+-filetype:xml+more:pagemap:metatags-prism.section&siteSearch=foxnews.com&siteSearchFilter=i&callback=__jp0'
    # params = {
    #     'q': keyword,
    #     'size': size
    # }
    res = requests.get(url, params=params).json()
    for d in res['result']:
        title = d['headline']
        img_url = d['thumbnail']
        article = d['body']
        new_article = str(article).replace(".", ". <br><br> ")
        content = {
            'title': title,
            'img_url': img_url,
            'article': new_article
        }
        data.append(content)

    return data
