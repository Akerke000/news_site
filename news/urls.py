from django.urls import path
from .views import Post_list, postDetails, addPost, editPost, deletePost

urlpatterns = [
    path('', Post_list, name = 'post_list'),
    path('<int:pid>/', postDetails, name='details'),
    path('add/', addPost, name='add-new-post'),
    path('<int:pid>/edit/', editPost, name='edit-post'),
    path('<int:pid>/delete/', deletePost, name='delete-post'),
]