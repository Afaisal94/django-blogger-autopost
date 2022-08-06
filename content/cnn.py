import requests


def get_cnn(keyword, post_num):
    data = []
    size = post_num * 10
    url = 'https://search.api.cnn.io/content?'
    params = {
        'q': keyword,
        'size': size
    }
    res = requests.get(url, params=params).json()
    for d in res['result']:
        title = d['headline']
        img_url = d['thumbnail']
        article = d['body']
        new_article = '<p>' + str(article).replace(".", ". </p><p> ")
        content = {
            'title': title,
            'img_url': img_url,
            'article': new_article
        }
        data.append(content)

    return data
