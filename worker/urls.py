from django.urls import path
from . import views


urlpatterns = [

    path('electricians',views.electricians, name = 'electricians'),
    path('cleaners',views.cleaners, name = 'cleaners'),
    path('shifters',views.shifters, name = 'shifters'),
    path('workers',views.workers, name = 'workers'),
    path('plumbers',views.plumbers, name = 'plumbers'),
    path('painters',views.painters, name = 'painters'),
    path('booking',views.booking, name = 'booking'),
    path('request',views.request, name = 'request'),

]
