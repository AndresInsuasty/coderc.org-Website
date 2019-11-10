from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import CommentForm

# Create your views here.
def blog(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form = CommentForm()
        print(form)
        blogs = Post.objects.all()
        comments = Comment.objects.all()
        return render(request,"blog/blog.html",{'blogs': blogs,'comments':comments,'form':form})