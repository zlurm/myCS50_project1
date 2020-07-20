from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:page_name>", views.wiki, name="wiki"),
    path("search", views.search, name="search"),
    path("new", views.new_page, name="new")
]
