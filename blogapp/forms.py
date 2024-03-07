from django import forms
from django.forms import ModelForm
from .models import Post, Category, Comment, About, Privacy, Terms


class CreateForm(ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'category', 'tags', 'content', 'image', 'image_credit', 'status']


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']


class AboutForm(ModelForm):
    class Meta:
        model = About
        fields = '__all__'

class PrivacyForm(ModelForm):
    class Meta:
        model = Privacy
        fields = '__all__'

class TermForm(ModelForm):
    class Meta:
        model = Terms
        fields = '__all__'

