from django.urls import path
from .views import AddPost, PostList, PostDetail, PostLike, \
    UpdatePostView, DeletePostView, UserEditView


urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('like/<slug:slug>/', PostLike.as_view(), name='post_like'),
    path('create/', AddPost.as_view(), name='create_post'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('edit/<slug:slug>/', UpdatePostView.as_view(), name='update_post'),
    path('<slug:slug>/delete/', DeletePostView.as_view(), name='delete'),
]
