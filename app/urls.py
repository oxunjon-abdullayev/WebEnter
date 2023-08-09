from django.urls import path

from app.views import index_view, blogs_view, blog_detail

urlpatterns = [
    path('', index_view, name='index'),
    path('blog-page/', blogs_view, name='blog-view'),
    path('blog-detail/<int:blog_id>/', blog_detail, name='blog-detail'),
]