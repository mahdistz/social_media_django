from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('new-post/', NewPost.as_view(), name='new_post'),
    path('postlist/', PostList.as_view(), name='post_list'),
    # path('new-comment/<int:id>', NewComment.as_view(), name='new-comment'),
    path('postdetail/<int:post_id>', PostDetail.as_view(), name='post_detail'),
    path('recently/', PostRecently.as_view(), name="post_recently"),
    # path('all_posts/', all_posts, name='all_posts'),
    # path('posts_of_user/<int:id>', posts_of_user, name='posts_of_user'),
    # path('post_information/<int:id>', post_information, name='post_information'),
    # path('all_users/', all_users, name='all_users'),
    # path('user_info/<int:id>', user_info, name='user_info'),
    # path("comments/<int:id>", comments, name='comments'),
]
