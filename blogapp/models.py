from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField
from django.utils import timezone
from django.utils.text import slugify
from taggit.managers import TaggableManager
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    class Meta:
        ordering=('-name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', args=[self.slug])
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            super(Category, self).save(*args, **kwargs)

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, null=True, related_name="posts", blank=True,
                                 on_delete=models.SET_NULL)
    tags = TaggableManager()
    content = HTMLField(blank=True, null=True)
    image = models.ImageField(upload_to='static/images', blank=True, null=True)
    image_credit = models.URLField(null=True, help_text="paste or type the link(optional)", blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog')
    slug = models.SlugField(max_length=100, unique=True)
    updated = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogapp:detail', args=[self.slug])

    class Meta:
        ordering = ['date_created']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80, null=True)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    parent = models.ForeignKey('self', null=True, related_name='replies', on_delete=models.CASCADE)

    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'



class About(models.Model):
    body = HTMLField(blank=True, null=True)

class Terms(models.Model):
    body = HTMLField(blank=True, null=True)

    class Meta:
        verbose_name = 'Terms'
        verbose_name_plural = 'Terms'

class Privacy(models.Model):
    body = HTMLField(blank=True, null=True)

    class Meta:
        verbose_name = 'Privacy'
        verbose_name_plural = 'Privacies'

