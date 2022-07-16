from django.contrib import admin
from django.urls import path, include
func = lambda : 0

urlpatterns = [
    path('admin/', admin.site.urls),
    path("favicon.ico", func),
    path("", include("shortener.urls")),
]
