from django.contrib import admin
from .models import Post
# Register your models here.

# admin.site.register(Post)

@admin.register(Post)
class ItemAdmin(admin.ModelAdmin):
    # list_display = ['pk']  #primary key일 경우 'pk'라는 별칭으로 대체할 수 있다. 
    list_display = ['id','message','message_length','created_at','updated_at']
    list_display_links = ['message']
    # pass 