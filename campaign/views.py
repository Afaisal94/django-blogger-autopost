from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from .forms import CampaignForm
from .models import Campaign
from blog.models import Blog
from mail.models import Mail
from content.models import Content
from report.models import Report
from django.contrib.auth.mixins import LoginRequiredMixin
# Send Email
from django.conf import settings
from django.core.mail import send_mail
import time

class CampaignIndex(LoginRequiredMixin, View):
    def get(self, request):
        campaigns = Campaign.objects.all()
        return render(request, 'campaign/index.html', {
            'campaigns': campaigns
        })

class CampaignDetail(LoginRequiredMixin, View):
    def get(self, request, id):
        campaign = Campaign.objects.get(pk=id)
        return render(request, 'campaign/detail.html', {
            'campaign': campaign
        })


class CampaignCreate(LoginRequiredMixin, View):
    def get(self, request):
        form = CampaignForm()
        return render(request, 'campaign/form.html', {
            'form': form
        })

    def post(self, request):
        form = CampaignForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Sukses Menambah Campaign baru.')
            return HttpResponseRedirect(reverse('campaign-index'))
        return render(request, 'campaign/form.html', {
            'form': form
        })

class CampaignUpdate(LoginRequiredMixin, View):
    def get(self, request, id):
        existing_data = Campaign.objects.get(pk=id)
        form = CampaignForm(instance=existing_data)
        return render(request, 'campaign/form.html', {
            'form': form
        })

    def post(self, request, id):
        existing_data = Campaign.objects.get(pk=id)
        form = CampaignForm(request.POST, instance=existing_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sukses Mengupdate Campaign.')
            return HttpResponseRedirect(reverse('campaign-index'))
        return render(request, 'campaign/form.html', {
            'form': form
        })

class CampaignDelete(LoginRequiredMixin, View):
    def get(self, request, id):
        campaign = get_object_or_404(Campaign, id=id)
        campaign.delete()
        messages.success(request, 'Sukses Menghapus Campaign.')
        return HttpResponseRedirect(reverse('campaign-index'))

class CampaignRun(View):
    def get(self, request, id):
        # VAR 1
        campaign = Campaign.objects.get(pk=id)
        blog = campaign.blog
        keyword = campaign.keyword

        # VAR 2
        blog = Blog.objects.get(blog=blog)
        email = Mail.objects.get(pk=blog.email_id)

        email_sender = email.email
        password_sender = email.password
        email_post = blog.email_post

        # LOOPING CONTENT BY KEYWORD - BERAPA BANYAK CONTENT (10)
        contents = Content.objects.filter(keyword=keyword)[:5]
        for content in contents:
            # SEND MAIL
            subject = content.title
            html_message = content.article
            send_mail(
                subject=subject,
                message=html_message,
                from_email=email_sender,
                recipient_list=[email_post, ],
                auth_user=email_sender,
                auth_password=password_sender,
                fail_silently=False,
                html_message=html_message
            )

            # DELETE CONTENT
            content = Content.objects.get(pk=content.id)
            content.delete()

            time.sleep(3)

        # INSERT REPORT
        report = Report(blog=blog, keyword=keyword, status='SUCCESS')
        report.save()

        time.sleep(5)

        messages.success(request, 'Sukses Run Campaign.')
        return HttpResponseRedirect(reverse('campaign-index'))

class CampaignRunAll(View):
    def get(self, request):
        # GET ALL
        campaigns = Campaign.objects.filter(status='ACTIVE')
        # LOOPING CAMPAIGNS
        for c in campaigns:
            id = c.id

            # VAR 1
            campaign = Campaign.objects.get(pk=id)
            blog = campaign.blog
            keyword = campaign.keyword

            # VAR 2
            blog = Blog.objects.get(blog=blog)
            email = Mail.objects.get(email=blog.email)

            email_sender = email.email
            password_sender = email.password
            email_post = blog.email_post

            # LOOPING CONTENT BY KEYWORD - BERAPA BANYAK CONTENT (10)
            contents = Content.objects.filter(keyword=keyword)[:5]
            for content in contents:
                # SEND MAIL
                subject = content.title
                html_message = content.article
                send_mail(
                    subject=subject,
                    message=html_message,
                    from_email=email_sender,
                    recipient_list=[email_post, ],
                    auth_user=email_sender,
                    auth_password=password_sender,
                    fail_silently=False,
                    html_message=html_message
                )

                # DELETE CONTENT
                content = Content.objects.get(pk=content.id)
                content.delete()

                time.sleep(3)

            # INSERT REPORT
            report = Report(blog=blog, keyword=keyword, status='SUCCESS')
            report.save()

            time.sleep(5)

        messages.success(request, 'Sukses Run Campaign.')
        return HttpResponseRedirect(reverse('campaign-index'))