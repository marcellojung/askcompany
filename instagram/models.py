from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model): 
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)  ##from django.contrib.auth.models import user 쓰는것보다 settings에 설정된 settings.AUTH_USER_MODEL을 쓰자.
    message = models.TextField()
    photo = models.ImageField(blank=True,upload_to='instagram/post/%Y/%m/%d')  #pillow 를 통해서 pil 관리. 이미지 관리 
    is_public = models.BooleanField(default=False,verbose_name='공개여부') #새로운 필드 추가하였음. makemigrtions, migrate 다 해줘야. 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Custom Post Object ({self.id},{self.message})"
    
    class Meta:
        ordering=['-id']

    def message_length(self):
        return len(self.message)
    message_length.short_description = "메시지 글자수"
    
    
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)