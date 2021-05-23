from django.shortcuts import render
from .models import Blog
# Create your views here.
def board(request):
    blogs = Blog.objects
    return render(request, 'blogapp/board.html', {'blogs':blogs})
    
def layout(request):
    return render(request, 'blogapp/layout.html')

def main(request):
    return render(request, 'blogapp/main.html')