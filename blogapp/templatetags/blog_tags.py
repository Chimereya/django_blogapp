from django import template

register = template.Library()

from ..models import Post


# latests posts
@register.inclusion_tag('blogapp/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.objects.filter(status=1).order_by('-date_created')[:count]
    return {'latest_posts': latest_posts}