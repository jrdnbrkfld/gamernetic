from .views import AddPost, PostList, PostDetail, PostLike
from django.urls import path


urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('like/<slug:slug>/', PostLike.as_view(), name='post_like'),
    path('add_post/', AddPost.as_view(), name='create_post'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
]
