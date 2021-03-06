from django import forms
from django.contrib.auth.models import User
from .models import Post

class PostFrom(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        filter = ["name"]