from django.db import models

# Create your models here.
class Post(models.Model):
    id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=50) # 100글자가 최대인 문자열
    content = models.TextField(null=True,blank=True) # 글자 수 제한이 없는 긴 문자열
    create_at = models.DateTimeField(auto_now_add=True) # 처음 Post 생성시, 현재시간 저장

    

class Member(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharFiled(max_length=20)
    email=models.EmailFiels(unique=True)

class Comment(models.Model):
    id=models.AutoField(primary_key=True)
    content = models.CharField(max_length=200,null=True,blank=True)
    post_id = models.ForeignKey(Post, verbose_name='Post', on_delete=models.CASCADE,related_name='comments')
    member_id = models.ForeignKey(Member,verbose_name = 'Member',on_delete=models.CASCADE,related_name='coments' )
    def  __str__(self):
        return self.content 


class UserPost(models.Model):
    user_id=models.ForeignKey(Member,verbose_name='Member',on_delete=models.CASCADE,related_name='user_posts')
    post_id=models.ForeignKey(Post,verbose_name='Post',on_delete=models.CASCADE,related_name='user_posts')

