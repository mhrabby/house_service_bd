from django.conf.urls import url,include
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

from HouseServiceBDapp import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name = 'home'),
    path('accounts/',include('accounts.urls')),
    path('worker/',include('worker.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
