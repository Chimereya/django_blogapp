from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('signup/', views.register_page, name='signup'),
    path('logout/', views.logout_page, name='logout'),

]