from django.shortcuts import render

# Create your views here.


def publications(request):
    return render(request, 'publications/publications_page.html')
