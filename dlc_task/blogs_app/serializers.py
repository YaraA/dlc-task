from django.contrib.auth.models import User
from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
    def create(self, validated_data):
       password = validated_data.pop("password")
       user = User.objects.create(**validated_data)
       if password:
           user.set_password(password)
           user.save()
       return user

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Blog
        fields = '__all__'

class AddUserToBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Blog
        fields = ['users']

class UsersOfBlogSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True)
    class Meta:
        model = models.Blog
        fields = ['users']

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = models.Post
        fields = ['id', 'content', 'number_of_likes', 'blog', 'owner']

class PostEditSerializer(serializers.ModelSerializer):
  class Meta:
        model = models.Post
        fields = ['content']
  
class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = models.Comment
        fields = ['id','content', 'number_of_likes', 'post', 'owner']

class CommentsOnPostSerializer(serializers.ModelSerializer):
    post = PostSerializer()
    class Meta:
        model = models.Comment
        fields = '__all__'

class CommentEditSerializer(serializers.ModelSerializer):
  class Meta:
        model = models.Comment
        fields = ['content']