from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('airpollution/', include('airpollution.urls'))
   ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
""" + static... -> to show app image on url in admin page
MEDIA_URL -> defined in settings.py MEDIA_URL = '/media/'

path('', include('website.urls')), -> url to website app
path('airpollution/', include('airpollution.urls')) -> url to airpollution app
"""
