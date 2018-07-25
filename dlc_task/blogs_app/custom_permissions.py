from rest_framework import permissions
from . import models
from django.contrib.auth.models import User

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

class canEditInfo(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.username == request.user.username

class canAddPost(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        blog = models.Blog.objects.get(id=obj.blog.id)
        users_of_blog = blog.users.all()
        curr_user = User.objects.get(id=request.user.id)

        if curr_user in users_of_blog:
            return True
        else: 
            return False

class canAddComment(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        # return obj.blog == request.user.id
        post = models.Post.objects.get(id=obj.post.id)
        blog_of_post = models.Blog.objects.get(id=post.blog.id)
        users_of_blog = blog_of_post.users.all()
        curr_user = User.objects.get(id=request.user.id)
        if curr_user in users_of_blog:
            return True
        else: 
            return False
