from django.shortcuts import render, HttpResponse, redirect
from .models import New, UserProfile

from . forms import RegisterUserForm, LoginForm, PostNewsForm

from django.contrib.auth import authenticate, login, logout

# Create your views here.

def main_page(request):
    news = New.objects.all()

    return render(request, 'index.html', context={'news': news})

def main_about(request):
    return render(request, 'abaut.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)

        if form.is_valid():
            user = form.save()

            UserProfile.objects.create(user=user)

            return redirect('login')

    else:
        form = RegisterUserForm()

    return render(request, 'registration/register.html', context={'form': form})




def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)

                return redirect('/')
    
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', context={'form': form})


def logout_user_view(request):
    logout(request)

    return redirect('/')

def create_news(request):
    if request.method == 'POST':
        form = PostNewsForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            tags = form.cleaned_data['tags']

            New.objects.create(news_title=title, desc=description, tags=tags).save()

            return redirect('/')
        
    else:
        form = PostNewsForm()

    return render(request, 'post_new.html', context={'form': form})