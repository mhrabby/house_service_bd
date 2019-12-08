from django.urls import path
from . import views


urlpatterns = [

    path('register',views.register, name = 'register'),
    path('animal', views.animal_view,name='animal'),
    path('login', views.login,name='login'),
    path('logout', views.logout,name='logout'),
]
