from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("xss/", views.xss, name='xss'),
    path("search", views.search, name="search"),
    path("labs", views.labs, name="labs")

]
