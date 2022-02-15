from django.urls import path
from .views import HomeView, DetailView, AddPostView, UpdatePostView, DeletePostView, CategoryView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("blog/<int:pk>", DetailView.as_view(), name="details"),
    path("add_post/", AddPostView.as_view(), name="add_post"),
    path("edit/<int:pk>", UpdatePostView.as_view(), name="update"),
    path("delete/<int:pk>", DeletePostView.as_view(), name="delete"),
    path("category/<str:teams>", CategoryView, name="category"),
]