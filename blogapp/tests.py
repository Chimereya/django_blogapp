from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post
from django.urls import reverse

class BlogTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='chimex',
            email='chimex@yahoo.com',
            password='secret',
        )

        self.post = Post.objects.create(
            title='this is a post',
            content='this is a content',
            author=self.user
        )

    def string_representation(self):
        post = Post(title='a post title')
        post.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'this is a post')
        self.assertEqual(f'{self.post.content}', 'this is a content')
        self.assertEqual(f'{self.post.author}', 'chimex')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogapp/home.html')





