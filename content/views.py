from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Content
from keywords.models import Keyword
from blog.models import Blog
from django.views import View
from .bbc import get_bbc
from .cnn import get_cnn
from .agc import get_agc
import datetime
import csv

# Send Email
from django.conf import settings
from django.core.mail import send_mail

# CONTENT NEWS

class ContentNewsIndex(LoginRequiredMixin, View):
    def get(self, request):
        # contents = Content.objects.all()
        contents = Content.objects.filter(type="NEWS")
        return render(request, 'content_news/index.html', {
            'contents': contents
        })

class ContentNewsDetail(LoginRequiredMixin, View):
    def get(self, request, id):
        content = Content.objects.get(pk=id)
        return render(request, 'content_news/detail.html', {
            'content': content
        })

class ContentNewsDelete(LoginRequiredMixin, View):
    def get(self, request, id):
        content = get_object_or_404(Content, id=id)
        content.delete()
        messages.success(request, 'Sukses Menghapus Content.')
        return HttpResponseRedirect(reverse('contentnews-index'))

class ScrapeContentNews(LoginRequiredMixin, View):
    def get(self, request):
        keywords = Keyword.objects.all()
        return render(request, 'content_news/scrape_content.html', {
            'keywords': keywords
        })

    def post(self, request):
        source = request.POST['source']
        keyword_id = request.POST['keyword_id']
        post_num = int(request.POST['post_num'])
        keyword = Keyword.objects.get(pk=keyword_id)
        type = 'NEWS'

        if source == 'bbc':
            data = get_bbc(keyword, post_num)
        else:
            data = get_cnn(keyword, post_num)

        for d in data:
            new_article = "<img src='" + d['img_url'] + "'> <br><br>" + d['article']
            permalink = str(d['title']).replace(' ', '-')
            c = Content(title=d['title'], img_url=d['img_url'], article=new_article, keyword_id=keyword_id, type=type, permalink=permalink)
            c.save()

        messages.success(request, 'Sukses Scraping Content.')
        return HttpResponseRedirect(reverse('contentnews-index'))

class ExportContentNews(LoginRequiredMixin, View):
    def get(self, request):
        blogs = Blog.objects.all()
        keywords = Keyword.objects.all()
        return render(request, 'content_news/export_content.html', {
            'keywords': keywords,
            'blogs': blogs
        })
    def post(self, request):
        blog_id = request.POST['blog_id']
        keyword_id = request.POST['keyword_id']
        jumlah_konten = int(request.POST['jumlah_konten'])
        type = 'AGC'

        # Format : blogger_url, title, content, permalink

        # NAME FILE
        kw = Keyword.objects.get(pk=keyword_id)
        key = kw.keyword
        key = str(key).replace(' ', '-') + '-'
        x = datetime.datetime.now()
        year = x.year
        month = x.month
        day = x.day
        ext = '.csv'
        filename = key + str(day) + str(month) + str(year) + ext

        blog = Blog.objects.get(pk=blog_id)
        url_blogger = blog.url_blogger

        contents = Content.objects.filter(keyword=keyword_id, type=type)[:jumlah_konten]

        csv_content  = []
        for content in contents:
            data = [url_blogger, content.title, content.article, content.title]
            csv_content.append(data)

        csv_file = open(filename, 'w', newline='')

        csv_writer = csv.writer(csv_file, delimiter=";")

        for row in csv_content:
            csv_writer.writerow(row)

        csv_file.close()

        messages.success(request, 'Sukses Export Content News.')
        return HttpResponseRedirect(reverse('contentnews-index'))

# CONTENT AGC

class ContentAgcIndex(LoginRequiredMixin, View):
    def get(self, request):
        # contents = Content.objects.all()
        contents = Content.objects.filter(type="AGC")
        return render(request, 'content_agc/index.html', {
            'contents': contents
        })

class ContentAgcDetail(LoginRequiredMixin, View):
    def get(self, request, id):
        content = Content.objects.get(pk=id)
        return render(request, 'content_agc/detail.html', {
            'content': content
        })

class ContentAgcDelete(LoginRequiredMixin, View):
    def get(self, request, id):
        content = get_object_or_404(Content, id=id)
        content.delete()
        messages.success(request, 'Sukses Menghapus Content.')
        return HttpResponseRedirect(reverse('contentagc-index'))

class ScrapeContentAgc(LoginRequiredMixin, View):
    def get(self, request):
        keywords = Keyword.objects.all()
        return render(request, 'content_agc/scrape_content.html', {
            'keywords': keywords
        })
    def post(self, request):
        keyword_id = request.POST['keyword_id']
        keywords = request.POST['keywords']
        type = 'AGC'
        kw = keywords.split('\n')
        for k in kw:
            contents = get_agc(k)
            c = Content(title=contents['title'], img_url=contents['img_url'], article=contents['article'], keyword_id=keyword_id, type=type,
                        permalink=contents['permalink'])
            c.save()

        messages.success(request, 'Sukses Scraping Content.')
        return HttpResponseRedirect(reverse('contentagc-index'))


class ExportContentAgc(LoginRequiredMixin, View):
    def get(self, request):
        blogs = Blog.objects.all()
        keywords = Keyword.objects.all()
        return render(request, 'content_agc/export_content.html', {
            'keywords': keywords,
            'blogs': blogs
        })
    def post(self, request):
        blog_id = request.POST['blog_id']
        keyword_id = request.POST['keyword_id']
        jumlah_konten = int(request.POST['jumlah_konten'])
        type = 'AGC'

        # Format : blogger_url, title, content, permalink

        # NAME FILE
        kw = Keyword.objects.get(pk=keyword_id)
        key = kw.keyword
        key = str(key).replace(' ', '-') + '-'
        x = datetime.datetime.now()
        year = x.year
        month = x.month
        day = x.day
        ext = '.csv'
        filename = key + str(day) + str(month) + str(year) + ext

        blog = Blog.objects.get(pk=blog_id)
        url_blogger = blog.url_blogger

        contents = Content.objects.filter(keyword=keyword_id, type=type)[:jumlah_konten]

        csv_content = []
        for content in contents:
            meta_desc = "If you're searching about " + str(content.title) + " you've came to right page. we have some information for you"

            data = [url_blogger, content.title, content.article, content.permalink, meta_desc]
            csv_content.append(data)

        csv_file = open(filename, 'w', newline='')

        csv_writer = csv.writer(csv_file, delimiter=";")

        for row in csv_content:
            csv_writer.writerow(row)

        csv_file.close()

        messages.success(request, 'Sukses Export Content AGC.')
        return HttpResponseRedirect(reverse('contentagc-index'))