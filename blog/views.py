from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, UpdateForm
from django.urls import reverse_lazy, reverse

# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = "home.html"
    # ordering = ["-id"]
    ordering = ["-post_date"]
    
class DetailView(DetailView):
    model = Post
    template_name = "details.html"
    
class AddPostView(CreateView):
    model = Post
    form_class = PostForm 
    template_name = "post.html"
    
class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = "update.html"

class DeletePostView(DeleteView):
    model = Post
    template_name = "delete.html"
    success_url = reverse_lazy("home")

def CategoryView(request, teams):
    category_posts = Post.objects.filter(category=teams)
    return render(request, "category.html", {"teams":teams, "category_posts":category_posts})