from .views import AddPostView, PostList, PostDetail, PostLike
from django.urls import path


urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>/', PostLike.as_view(), name='post_like'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
]
