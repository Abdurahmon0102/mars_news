from django.urls import path
from .views import main_page, main_about, register_view, login_view, create_news, logout_user_view

urlpatterns = [
    path('', main_page),
    path('about/', main_about, name='about'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_user_view, name='logout'),
    path('post-new/', create_news, name='post-new'),
    
]