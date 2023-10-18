from django.shortcuts import render


# Create your views here.

def register(request):
    return render(request, 'accounts/register_page.html')


def login(request):
    return render(request, 'accounts/login_page.html')
