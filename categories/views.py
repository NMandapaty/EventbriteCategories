from django.shortcuts import render
from django.http import HttpResponse
from . import services

# Create your views here.

def index(request):
    if request.method == "GET":
        cats, error = services.get_categories()
        if error:
            return HttpResponse(error)

        return render(request, 'search.html',
                      context={'categories': cats})

def events(request):
    if request.method == "GET":
        choices = [
            request.GET.get('c1', ''),
            request.GET.get('c2', ''),
            request.GET.get('c3', '')
        ]
        page = int(request.GET.get('page', '1'))

        events, page_count, error = services.get_events(choices, page=page)
        if error:
            return HttpResponse(error)

        return render(request, 'events.html',
                      context={'events': events, 'page_count': page_count, 'current_page': page})
