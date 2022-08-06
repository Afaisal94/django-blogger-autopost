from bing_image_urls import bing_image_urls
from duckduckgo_search import ddg
import time


def get_agc(keyword):
    permalink = str(keyword).replace(' ', '-')
    meta_desc = "<p>If you're searching about " + str(keyword) + " you've came to right page. we have some information for you </p><br><br>"
    # IMAGE
    images = bing_image_urls(keyword, limit=2)
    img_url = images[0]
    img = '<center><img src="' + str(img_url) + '"></center><br><br>'
    # ARTICLE
    paragraph = []
    results = ddg(keyword, region='wt-wt', safesearch='Moderate', time='y', max_results=5)
    for r in results:
        body = r['body']
        paragraph.append(body)
    content = '<p>'
    for p in paragraph:
        content = content + str(p) + '</p><p>'
    article = meta_desc + str(img) + str(content)

    content = {
        'title': keyword,
        'img_url': img_url,
        'article': article,
        'permalink': permalink
    }

    return content
