from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("create", views.create_url, name="create"),
    path("<str:uuid>", views.get_real_url, name="get_url"),
]