from django.urls import path

from . import views
from .views import AddPostView

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("posts", views.AllPostsView.as_view(), name="posts-page"),
    path("posts/<slug:slug>", views.SinglePostView.as_view(),
         name="post-detail-page"),  # /posts/my-first-post
    path("read-later", views.ReadLaterView.as_view(), name="read-later"),
    path('add_post/', AddPostView.as_view(), name='add_post'),

]