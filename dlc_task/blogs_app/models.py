from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
  title = models.TextField(unique=True)
  description = models.TextField()
  users = models.ManyToManyField(User)
  class Meta:  
        db_table = "blog"  

class Post(models.Model):
  content = models.TextField()
  number_of_likes = models.IntegerField(default=0)
  owner = models.ForeignKey(User, on_delete=models.CASCADE)

  blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
  class Meta:  
        db_table = "post" 

class Comment(models.Model):
  content = models.TextField()
  number_of_likes = models.IntegerField(default=0)
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  owner = models.ForeignKey(User, on_delete=models.CASCADE)
  class Meta:  
        db_table = "comment" 