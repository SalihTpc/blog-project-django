# from unicodedata import category
from django import forms
from .models import Post, Category

# choices = Category.objects.all().values_list("name", "name")

# choice_list = [choice for choice in choices]

category = forms.ModelChoiceField(queryset=Category.objects.all())

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title","author", "category", "body", "image")
        widgets = {
            # "title": forms.TextInput(attrs={"class":"form-control", "placeholder":"This is Title PlaceHolder"}),
            "title": forms.TextInput(attrs={"class":"form-control"}),
            "author": forms.TextInput(attrs={"class":"form-control", "value":"", "id":"user", "type":"hidden"}),
            "category": forms.Select(attrs={"class":"form-control"}),
            # "category": forms.ModelChoiceField(queryset=Category.objects.all()),
            "body": forms.Textarea(attrs={"class":"form-control"}),
            "image": forms.TextInput(attrs={"class":"form-control", "placeholder":"Post picture url should be add"}),
        }
        
class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "category", "body", "image")
        widgets = {
            "title": forms.TextInput(attrs={"class":"form-control"}),
            "category": forms.Select(attrs={"class":"form-control"}),
            # "category": forms.ModelChoiceField(queryset=Category.objects.all()),
            "body": forms.Textarea(attrs={"class":"form-control"}),
            "image": forms.TextInput(attrs={"class":"form-control" , "placeholder":"Post picture url should be add"}),
        }