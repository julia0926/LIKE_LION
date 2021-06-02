from django.db import models
from django.conf import settings
# Create your models here.
class Blog(models.Model): #
    title = models.CharField(max_length=200) #글 제목 
    writer = models.CharField(max_length=100,default='작성자를 적어주세요.') #글 작성자
    pub_date = models.DateTimeField('data published') #글 쓰는 시각
    content = models.TextField() #글 내용 (글자수 제한없이 )

    def __str__(self): #글 제목을 자신으로 받아서 넣음
        return self.title

class Comment(models.Model):
    def __str__(self):
        return self.text
    
    post_id=models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    text=models.CharField(max_length=50)
