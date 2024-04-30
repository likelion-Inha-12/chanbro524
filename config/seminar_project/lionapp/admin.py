from django.contrib import admin

# Register your models here.
from .models import Post
from .models import Comment
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)