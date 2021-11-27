from django.shortcuts import render


# Create your views here.

def welcome(request):
    context = {
        'page': request.path
    }
    return render(request, 'airpollution/welcome.html', context)


""" we pass context -> if the page request.path is /airpollution, do this in navbar, or
 do something else in navbar"""
