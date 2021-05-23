from django.shortcuts import redirect, render,get_object_or_404 
from django.utils import timezone
from .models import Blog
# Create your views here.

def main(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/main.html', {'blogs' :blogs})

def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.writer = request.POST['writer']
    new_blog.content = request.POST['content']
    new_blog.pub_date = timezone.now()
    new_blog.save()
    return redirect('detail', new_blog.id)

def detail(request, id): # 이것도 마찬가지로 해당 글만 나와야 하므로 id를 매개변수로 받아옴
    blog = get_object_or_404(Blog, pk = id) 
    # id값이 있는 해당 데이터를 가져오거나 데이터가 없을 경우에 404에러를 띄우라는 의미
    # pk = primary key (기본키)
    return render(request, 'blog/detail.html', {'blog' : blog})

def write(request):
    return render(request, 'blog/write.html')

def edit(request, id):
    edit_blog=Blog.objects.get(id = id)
    return render(request, 'blog/edit.html',{'blog':edit_blog})


def update(request, id):
    update_blog = Blog.objects.get(id = id)
    update_blog.title = request.POST['title']
    update_blog.writer = request.POST['writer']
    update_blog.content = request.POST['content']
    update_blog.pub_date = timezone.now()
    update_blog.save()
    return redirect('detail', update_blog.id)

def delete(request, id):
    delete_blog=Blog.objects.get(id=id)
    delete_blog.delete()
    return redirect('main')
