from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Blog
from .forms import BlogForm
from django.views import View

class BlogIndex(LoginRequiredMixin, View):
    def get(self, request):
        blogs = Blog.objects.all()
        return render(request, 'blog/index.html', {
            'blogs': blogs
        })

class BlogDetail(LoginRequiredMixin, View):
    def get(self, request, id):
        blog = Blog.objects.get(pk=id)
        return render(request, 'blog/detail.html', {
            'blog': blog
        })


class BlogCreate(LoginRequiredMixin, View):
    def get(self, request):
        form = BlogForm()
        return render(request, 'blog/form.html', {
            'form': form
        })

    def post(self, request):
        form = BlogForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Sukses Menambah Blog baru.')
            return HttpResponseRedirect(reverse('blog-index'))
        return render(request, 'blog/form.html', {
            'form': form
        })

class BlogUpdate(LoginRequiredMixin, View):
    def get(self, request, id):
        existing_data = Blog.objects.get(pk=id)
        form = BlogForm(instance=existing_data)
        return render(request, 'blog/form.html', {
            'form': form
        })

    def post(self, request, id):
        existing_data = Blog.objects.get(pk=id)
        form = BlogForm(request.POST, instance=existing_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sukses Mengupdate Blog.')
            return HttpResponseRedirect(reverse('blog-index'))
        return render(request, 'blog/form.html', {
            'form': form
        })

class BlogDelete(LoginRequiredMixin, View):
    def get(self, request, id):
        blog = get_object_or_404(Blog, id=id)
        blog.delete()
        messages.success(request, 'Sukses Menghapus Blog.')
        return HttpResponseRedirect(reverse('blog-index'))