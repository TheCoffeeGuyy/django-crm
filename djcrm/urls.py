from django.contrib import admin
from django.urls import path
from leads.views import homePage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePage),
]
