from .views import AddPost, PostList, PostDetail, PostLike
from django.urls import path


urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>/', PostLike.as_view(), name='post_like'),
    path('summernote/add_post/', AddPost.as_view(), name='create_post'),
]
