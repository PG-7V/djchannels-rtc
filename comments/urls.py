from django.urls import path

from .views import CommentCreateView

urlpatterns = [
    path('create/<str:content_type>/<int:object_id>/', CommentCreateView.as_view(), name='comment-create')
]

app_name = 'comments'
