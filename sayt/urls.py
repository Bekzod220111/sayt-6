from django.urls import path
from . import views

urlpatterns = [
    path('index.html', views.index, name='index'),
    path('blog.html', views.blog, name='blog'),
    path('blog-detail/', views.blog_detail, name='blog-detail'),
    path('contact/', views.contact, name='contact'),
    path('project-detail/', views.project_detail, name='project-detail'),
]