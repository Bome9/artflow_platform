from django.shortcuts import render

# Create your views here.


def main(request):
    return render(request, 'main/main_page.html')


def publications(request):
    return render(request, 'main/publications_page.html')


def settings(request):
    return render(request, 'main/settings_page.html')


def profile_bio(request):
    return render(request, 'main/profile_bio_page.html')

