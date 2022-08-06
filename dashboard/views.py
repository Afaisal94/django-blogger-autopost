from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from mail.models import Mail
from blog.models import Blog
from keywords.models import Keyword
from content.models import Content
from campaign.models import Campaign
from report.models import Report

class DashboardIndex(LoginRequiredMixin, View):
    def get(self, request):
        email = len(Mail.objects.all())
        blog = len(Blog.objects.all())
        keyword = len(Keyword.objects.all())
        content_news = len(Content.objects.filter(type='NEWS'))
        content_agc = len(Content.objects.filter(type='AGC'))
        campaign = len(Campaign.objects.all())
        report = len(Report.objects.all())

        return render(request, 'dashboard/index.html', {
            'email': email,
            'blog': blog,
            'keyword': keyword,
            'content_news': content_news,
            'content_agc': content_agc,
            'campaign': campaign,
            'report': report
        })