from django.shortcuts import redirect, render,get_object_or_404 
from django.utils import timezone
from .forms import PostForm
from .models import Blog
# Create your views here.

#메인페이지
def main(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/main.html', {'blogs':blogs})

# 글 작성 페이지 
def write(request):
    return render(request, 'blog/write.html')

#글 작성 함수
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            form.pub_date=timezone.now()
            form.save()
            return redirect('main')
    else:
        form=PostForm
        return render(request,'blog/write.html',{'form':form})

# 디테일 페이지
def detail(request, id): 
    blog = get_object_or_404(Blog, pk = id) 
    return render(request, 'blog/detail.html', {'blog' : blog})

#수정페이지
def edit(request,id):
    post = get_object_or_404(Blog,id=id)
    if request.method == 'POST':
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('main')
    else:
        form=PostForm(instance=post)
        return render(request, 'blog/edit.html',{'form':form})

#삭제페이지
def delete(request, id):
    delete_blog=Blog.objects.get(id=id)
    delete_blog.delete()
    return redirect('main')
