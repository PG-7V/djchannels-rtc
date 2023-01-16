from django.urls import path

from .views import PostListView, PostDetailView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts'),
    path('posts/<str:post_slug>/', PostDetailView.as_view(), name='post')
]
