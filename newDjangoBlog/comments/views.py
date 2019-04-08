from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Post
# Create your views here.


from .models import Comment
from .forms import CommentForm



def post_comment(request, post_pk):
    post = get_object_or_404(Post, post_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) #提交实例，但不保存
            comment.post = post  #关联post
            comment.save()  #保存进数据库
            return redirect(post) #当 redirect 函数接收一个模型的实例时，它会调用这个模型实例的 get_absolute_url 方法，然后重定向到 get_absolute_url 方法返回的 URL。
        else:
            comment_list = post.comment_set.all() #等价于 Comment.objects.filter(post=post)，即根据 post 来过滤该 post 下的全部评论
            context = {
                'post':post,
                'form':form,
                'comment_list':comment_list,
            }
            return render(request, 'blog/detail.html', context=context)
















