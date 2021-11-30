from django.shortcuts import render


# Create your views here.

def welcome(request):
    context = {
        'app_name': request.resolver_match.app_name
    }

    return render(request, 'airpollution/welcome.html', context)


""" we pass context -> if the page request.path is /airpollution, do this in navbar, or
 do something else in navbar"""


def upload_file(request):
    context = {
        'app_name': request.resolver_match.app_name,
        'message_success': 'File uploaded successfully'
    }
    return render(request, 'airpollution/welcome.html', context)
