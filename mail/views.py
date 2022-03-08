from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Mail
from .forms import MailForm
from django.views import View

class MailIndex(LoginRequiredMixin, View):
    def get(self, request):
        mails = Mail.objects.all()
        return render(request, 'mail/index.html', {
            'mails': mails
        })

class MailDetail(LoginRequiredMixin, View):
    def get(self, request, id):
        mail = Mail.objects.get(pk=id)
        return render(request, 'mail/detail.html', {
            'mail': mail
        })


class MailCreate(LoginRequiredMixin, View):
    def get(self, request):
        form = MailForm()
        return render(request, 'mail/form.html', {
            'form': form
        })

    def post(self, request):
        form = MailForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Sukses Menambah Mail baru.')
            return HttpResponseRedirect(reverse('mail-index'))
        return render(request, 'mail/form.html', {
            'form': form
        })

class MailUpdate(LoginRequiredMixin, View):
    def get(self, request, id):
        existing_data = Mail.objects.get(pk=id)
        form = MailForm(instance=existing_data)
        return render(request, 'mail/form.html', {
            'form': form
        })

    def post(self, request, id):
        existing_data = Mail.objects.get(pk=id)
        form = MailForm(request.POST, instance=existing_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sukses Mengupdate Mail.')
            return HttpResponseRedirect(reverse('mail-index'))
        return render(request, 'mail/form.html', {
            'form': form
        })

class MailDelete(LoginRequiredMixin, View):
    def get(self, request, id):
        mail = get_object_or_404(Mail, id=id)
        mail.delete()
        messages.success(request, 'Sukses Menghapus Mail.')
        return HttpResponseRedirect(reverse('mail-index'))