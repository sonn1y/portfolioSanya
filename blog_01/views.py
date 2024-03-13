from django.shortcuts import render


def home(request):
    return render(request, 'blog_01/home.html')
# Create your views here.
