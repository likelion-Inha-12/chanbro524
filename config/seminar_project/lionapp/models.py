from django.db import models

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

class Member(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=200, null=True, blank=True)
    post = models.ForeignKey(Post, verbose_name='Post', on_delete=models.CASCADE, related_name='comments')
    member = models.ForeignKey(Member, verbose_name='Member', on_delete=models.CASCADE, related_name='member_comments', null=True)
    
    def __str__(self):
        return self.content 

class UserPost(models.Model):
    user_id = models.ForeignKey(Member, verbose_name='Member', on_delete=models.CASCADE, related_name='user_posts')
    post_id = models.ForeignKey(Post, verbose_name='Post', on_delete=models.CASCADE, related_name='user_posts')