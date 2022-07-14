from django.urls import path
from . import views

# url conf
urlpatterns = [
    # no need to add playground here as we have already 
    # added that in the main urls file
    path('home/',views.home),
    path('music/',views.music),
    path('videos/',views.videos),
    path('contact/',views.contact),
    path('playlist/',views.playlist),
    path('settings/',views.settings),
    
    ]
