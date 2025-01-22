from django.urls import path
from . import views
urlpatterns=[
    path('get/',views.get),
    path('redirect1/',views.redirect1),
    path('redirect2/',views.redirect2),
    path('builtinfields/',views.built),
    path('sucess/',views.thanku),
    path('form/',views.show),
]