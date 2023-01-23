from django.db import models

# Create your models here.
class Post(models.Model):
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