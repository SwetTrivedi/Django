from django.urls import path
from . import views
urlpatterns=[
    path('modelform/',views.md),
    path('save/',views.saved),
    path('match/',views.matching),
    path('builtinvalidate/',views.builtinvalidate),
    path('cleanvalidate2/',views.cleanvalidate2),
    path('cleanvalidate1/',views.cleanvalidate1),
    path('get/',views.get),
    path('redirect1/',views.redirect1),
    path('redirect2/',views.redirect2),
    path('builtinfields/',views.built),
    path('sucess/',views.thanku),
    path('form/',views.show),
]