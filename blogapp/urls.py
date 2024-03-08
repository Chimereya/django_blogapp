from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name= 'blogapp'

urlpatterns = [
    path('about/', views.about_view, name='about'),
    path('terms/', views.terms_view, name='terms'),
    path('privacy/', views.privacy_view, name='privacy'),
    path('create/', views.CreatePostView.as_view(), name='create'),
    path('', views.home_view, name='home'),
    path('<slug:slug>/', views.detail_view, name='detail'),
    path('category/<slug:category_slug>/', views.category_view, name='category'),
    path('tags/<slug:tag_slug>/', views.home_view, name='posts_by_tag'),
    path('edit/<int:pk>/', views.EditView.as_view(), name='edit'),
    path('delete/<int:pk>/', views.Delete.as_view(), name='delete'),
    path('create/add_category/', views.CreateCategoryView.as_view(), name='add_category'),
    path('add_bookmark/<slug:slug>/', views.add_bookmark, name='add_bookmark'),
    path('remove_bookmark/<slug:slug>/', views.remove_bookmark, name='remove_bookmark'),
    path('post/bookmarks/', views.bookmarked_posts, name='bookmarks'),

]

