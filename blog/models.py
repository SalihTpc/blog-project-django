from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    # image = models.ImageField(upload_to="")
    image = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default="1")
    likes = models.ManyToManyField(User, related_name="posts", blank=True)
    # slug = models.SlugField(blank=True, unique=True)
    
#     # def total_likes(self):
#     #     return self.likes.count()
    
    
    def __str__(self):
        return self.title + " | " + str(self.author)

    def get_absolute_url(self):
        # return reverse("details", args=(str(self.id)))
        return reverse("home")