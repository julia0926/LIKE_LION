from django import forms
from .models import Blog

class PostForm(forms.ModelForm):
    class Meta:
        model = Blog #Blog 모델을 참조해서 model을 만듬 
        fields = ['title', 'writer', 'content'] #모델 값은 이러함.