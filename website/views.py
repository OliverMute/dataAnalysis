from django.shortcuts import render
from website.models import MyApp


# Create your views here.

def index(request):
    all_apps = MyApp.objects.all()
    """Get all of the entries for this models
    all_apps -> it's a query like in SQL"""
    context = {
        'my_apps': all_apps,
        'view_name': request.resolver_match.view_name
    }
    """ access 'my_apps' context in HTML
    ex: when we loop, we use 'my_apps' -> for app in my_apps"""
    return render(request, 'website/index.html', context)
