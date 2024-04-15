from django.contrib import admin
from django.urls import path, include
from rest import urls as rest_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(rest_urls)),
]
