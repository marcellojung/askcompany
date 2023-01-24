from django.contrib import admin
from .models import Post, Comment
from django.utils.safestring import mark_safe  #안전하다. 자동 import 필요 
# Register your models here.

# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # list_display = ['pk']  #primary key일 경우 'pk'라는 별칭으로 대체할 수 있다. 
    list_display = ['id','message','message_length','photo_tag','is_public','created_at','updated_at']  #보여주는 부분
    list_display_links = ['message']  # 링크를 달아줌 
    list_filter = ['created_at','is_public']
    search_fields=['message']   #message 필드에서 필터를 제공하겠다. 
    # pass 
    def photo_tag(self,post):
        if post.photo: 
            # post.photo.url '
            return mark_safe(f'<img src="{post.photo.url}" styles="width: 36px;"/>')  #photo가 있다면 img url을 리턴하라. 
        return None
    
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

 