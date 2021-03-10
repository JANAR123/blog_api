from django.db import models

# Create your models here.


class Tag(models.Model):
    name=models.CharField(max_length=50,verbose_name="Теги") 
    def __str__(self):
        return f"{self.name}"
    class Meta:
        
        verbose_name="Тегги"
        verbose_name_plural="Тегги"

class Post(models.Model):
    title=models.CharField(max_length=100,verbose_name="Заголовок")
    body=models.TextField(max_length=200,verbose_name="Тело поста")
    tags=models.ManyToManyField(Tag,related_name="post",verbose_name="Теги")
    
    def __str__(self):
        return f"{self.title}"

        
    class Meta:
        verbose_name="Посты"
        verbose_name_plural="Посты"





   