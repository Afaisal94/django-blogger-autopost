from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Content
from keywords.models import Keyword
from django.views import View
from .bbc import get_bbc
from .cnn import get_cnn

# Send Email
from django.conf import settings
from django.core.mail import send_mail

class ContentIndex(LoginRequiredMixin, View):
    def get(self, request):
        contents = Content.objects.all()
        return render(request, 'content/index.html', {
            'contents': contents
        })

class ContentDetail(LoginRequiredMixin, View):
    def get(self, request, id):
        content = Content.objects.get(pk=id)
        return render(request, 'content/detail.html', {
            'content': content
        })

class ContentDelete(LoginRequiredMixin, View):
    def get(self, request, id):
        content = get_object_or_404(Content, id=id)
        content.delete()
        messages.success(request, 'Sukses Menghapus Content.')
        return HttpResponseRedirect(reverse('content-index'))

class ScrapeContent(LoginRequiredMixin, View):
    def get(self, request):
        keywords = Keyword.objects.all()
        return render(request, 'content/scrape_content.html', {
            'keywords': keywords
        })

    def post(self, request):
        source = request.POST['source']
        keyword_id = request.POST['keyword_id']
        post_num = int(request.POST['post_num'])
        keyword = Keyword.objects.get(pk=keyword_id)

        if source == 'bbc':
            data = get_bbc(keyword, post_num)
        else:
            data = get_cnn(keyword, post_num)

        for d in data:
            new_article = "<img src='" + d['img_url'] + "'> <br><br>" + d['article']
            c = Content(title=d['title'], img_url=d['img_url'], article=new_article, keyword_id=keyword_id)
            c.save()

        messages.success(request, 'Sukses Scraping Content.')
        return HttpResponseRedirect(reverse('content-index'))

class ImportContent(LoginRequiredMixin, View):
    def get(self, request):
        keywords = Keyword.objects.all()
        return render(request, 'content/import_content.html', {
            'keywords': keywords
        })

    def post(self, request):
        pass