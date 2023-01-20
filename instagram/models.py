from django.db import models

# Create your models here.
class Post(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Custom Post Object ({self.id},{self.message})"
    
    def message_length(self):
        return len(self.message)
    message_length.short_description = "메시지 글자수"