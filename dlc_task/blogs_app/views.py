from django.http import HttpResponse
from django.views.generic import TemplateView
from rest_framework import viewsets, generics, permissions
from django.contrib.auth.models import User
from . import custom_permissions
from . import models
from . import serializers

# Create your views here.

class UserCreateView(generics.CreateAPIView):
  serializer_class = serializers.UserSerializer

class UserEditInfoView(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, custom_permissions.canEditInfo, )
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class BlogCreateView(generics.CreateAPIView):
  serializer_class = serializers.BlogSerializer

class BlogsListView(generics.ListAPIView):
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer

class BlogAddUserView(generics.RetrieveAPIView):
    serializer_class = serializers.BlogSerializer
    def get_queryset(self):
      user_id = self.kwargs['user_id']
      blog_id = self.kwargs['pk']
      blog = models.Blog.objects.get(id=blog_id).users.add(user_id)
      return models.Blog.objects.filter(id=blog_id)

class BlogDetailView(generics.RetrieveAPIView):
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer

class BlogUsersView(generics.RetrieveAPIView):
  serializer_class = serializers.UsersOfBlogSerializer
  def get_queryset(self):
    blog_id = self.kwargs['pk']
    return models.Blog.objects.filter(id=blog_id)

class PostsOfUserView(generics.ListAPIView):
  serializer_class = serializers.PostSerializer
  def get_queryset(self):
    user_id = self.kwargs['user_id']
    return models.Post.objects.filter(owner=user_id)

class PostsOnBlogView(generics.ListAPIView):
  serializer_class = serializers.PostSerializer
  def get_queryset(self):
    blog_id = self.kwargs['blog_id']
    return models.Post.objects.filter(blog=blog_id)

class PostEditView(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, custom_permissions.IsOwnerOrReadOnly,)
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostEditSerializer

class PostDeleteView(generics.RetrieveDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, custom_permissions.IsOwnerOrReadOnly,)
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer

class AddPostView(generics.CreateAPIView):
    # permission_classes = ( custom_permissions.canAddPost,)
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    def perform_create(self, serializer):
      serializer.save(owner=self.request.user)

class AddCommentView(generics.CreateAPIView):
    # permission_classes = ( custom_permissions.canAddComment,)
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    def perform_create(self, serializer):
      serializer.save(owner=self.request.user)

class CommentsOfUserView(generics.ListAPIView):
  serializer_class = serializers.CommentsOnPostSerializer
  def get_queryset(self):
    user_id = self.kwargs['user_id']
    return models.Comment.objects.filter(owner=user_id)

class CommentEditView(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, custom_permissions.IsOwnerOrReadOnly,)
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentEditSerializer

class CommentDeleteView(generics.RetrieveDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, custom_permissions.IsOwnerOrReadOnly,)
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
