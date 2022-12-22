from django.contrib import admin
from django.urls import path, include

from Mainapp.views import home

urlpatterns = [
    # url 'admin/'
    path('admin/', admin.site.urls),

    # url 'home/'
    path('', home, name='home'),

    # include accounts urls
    path('', include('Mainapp.urls')),
]