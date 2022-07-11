from .views import AddPost, PostList, PostDetail, PostLike, UpdatePostView, DeletePostView, AboutUsView
from django.urls import path


urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('like/<slug:slug>/', PostLike.as_view(), name='post_like'),
    path('about/', AboutUsView.as_view(), name='about_us'),
    path('create/', AddPost.as_view(), name='create_post'),
    path('edit/<slug:slug>/', UpdatePostView.as_view(), name='update_post'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/delete/', DeletePostView.as_view(), name='delete'),
]
