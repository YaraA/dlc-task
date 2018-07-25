"""dlc_task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from .blogs_app import views

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^user/create/$', views.UserCreateView.as_view(), name="user_create"),
    url(r'^blog/create/$', views.BlogCreateView.as_view(), name="blog_create"),
    url(r'^blogs/list/$', views.BlogsListView.as_view(), name="blogs_list"),
    url(r'^blog/(?P<pk>\d+)/detail/$', views.BlogDetailView.as_view(), name="blog_detail"),
    url(r'^blog/(?P<pk>\d+)/users/$', views.BlogUsersView.as_view(), name="blog_users"),
    url(r'^blog/(?P<blog_id>\d+)/posts/$', views.PostsOnBlogView.as_view(), name="blog_posts"),
    url(r'^blog/(?P<pk>\d+)/user/(?P<user_id>\d+)/$', views.BlogAddUserView.as_view(), name="add_user_to_blog"),
    url(r'^user/(?P<pk>\d+)/update/$', views.UserEditInfoView.as_view(), name="user_edit_info"),
    url(r'^user/(?P<user_id>\d+)/posts/$', views.PostsOfUserView.as_view(), name="user_posts"),
    url(r'^user/(?P<user_id>\d+)/comments/$', views.CommentsOfUserView.as_view(), name="user_comments"),
    url(r'^post/add/$', views.AddPostView.as_view(), name="add_post"),
    url(r'^post/(?P<pk>\d+)/update/$', views.PostEditView.as_view(), name="post_edit"),
    url(r'^post/(?P<pk>\d+)/delete/$', views.PostDeleteView.as_view(), name="post_delete"),
    url(r'^comment/(?P<pk>\d+)/update/$', views.CommentEditView.as_view(), name="comment_edit"),
    url(r'^comment/(?P<pk>\d+)/delete/$', views.CommentDeleteView.as_view(), name="comment_delete"),
    url(r'^comment/add/$', views.AddCommentView.as_view(), name="add_comment")



]
