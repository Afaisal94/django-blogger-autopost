from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Keyword
from .forms import KeywordForm
from django.views import View

class KeywordIndex(LoginRequiredMixin, View):
    def get(self, request):
        keywords = Keyword.objects.all()
        return render(request, 'keyword/index.html', {
            'keywords': keywords
        })

class KeywordDetail(LoginRequiredMixin, View):
    def get(self, request, id):
        keyword = Keyword.objects.get(pk=id)
        return render(request, 'keyword/detail.html', {
            'keyword': keyword
        })


class KeywordCreate(LoginRequiredMixin, View):
    def get(self, request):
        form = KeywordForm()
        return render(request, 'keyword/form.html', {
            'form': form
        })

    def post(self, request):
        form = KeywordForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Sukses Menambah Keyword baru.')
            return HttpResponseRedirect(reverse('keyword-index'))
        return render(request, 'keyword/form.html', {
            'form': form
        })

class KeywordUpdate(LoginRequiredMixin, View):
    def get(self, request, id):
        existing_data = Keyword.objects.get(pk=id)
        form = KeywordForm(instance=existing_data)
        return render(request, 'keyword/form.html', {
            'form': form
        })

    def post(self, request, id):
        existing_data = Keyword.objects.get(pk=id)
        form = KeywordForm(request.POST, instance=existing_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sukses Mengupdate Keyword.')
            return HttpResponseRedirect(reverse('keyword-index'))
        return render(request, 'keyword/form.html', {
            'form': form
        })

class KeywordDelete(LoginRequiredMixin, View):
    def get(self, request, id):
        keyword = get_object_or_404(Keyword, id=id)
        keyword.delete()
        messages.success(request, 'Sukses Menghapus Keyword.')
        return HttpResponseRedirect(reverse('keyword-index'))