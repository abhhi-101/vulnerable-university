from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("xss", views.xss_lab, name='xss'),
    path("bruteforce", views.bruteforce, name='bruteforce'),
    path("search", views.search, name="search"),
    path("labs", views.labs, name="labs"),
    path("sxss", views.change_username, name="sxss"),
    path("csrf", views.csrf_lab, name="csrf"),
    path("clickjacking", views.clickjacking, name="clickjacking"),
    path("access_control", views.access_control, name="brokenAccessControl"),
    path("sen_info", views.sen_info, name="sen_info"),
    path("cmd", views.cmd, name="command_injection"),
    path("cmd_lab", views.cmd_lab, name="command_injection_lab"),
    path("db", views.db, name="db_injection"),
    path("db_info", views.db_info, name="db")
]
