from django.urls import path
from . import views

app_name = "meditation"

urlpatterns = [
    path('', views.meditation_page, name="page"),
]