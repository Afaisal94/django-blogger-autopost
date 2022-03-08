from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse('dashboard-index'))
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {
        'form': form
    })