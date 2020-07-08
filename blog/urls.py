from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('blog/detail/', views.BlogDetailView.as_view(), name='blog_detail'),
]
