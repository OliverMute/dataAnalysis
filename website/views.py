from django.shortcuts import render
from . models import MyApp


# Create your views here.

def index(request):
    all_apps = MyApp.objects.all()
    """Get all of the entries for this models"""
    context = {
        'my_apps': all_apps
    }
    """ access in HTML"""
    return render(request, 'website/index.html', context)
