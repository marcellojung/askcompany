from django.contrib import admin
from .models import Post
# Register your models here.

# admin.site.register(Post)

@admin.register(Post)
class ItemAdmin(admin.ModelAdmin):
    # list_display = ['pk']  #primary key일 경우 'pk'라는 별칭으로 대체할 수 있다. 
    list_display = ['id','message','message_length','is_public','created_at','updated_at']  #보여주는 부분
    list_display_links = ['message']  # 링크를 달아줌 
    list_filter = ['is_public']
    search_fields=['message']   #message 필드에서 필터를 제공하겠다. 
    # pass 