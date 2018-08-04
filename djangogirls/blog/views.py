from django.shortcuts import render
from django.utils import timezone
from .models import Post
#현재 디렉토리에 있는 모델스라는 파일에서 포스트 모델을 가져온다.
#포스트 모델에서 블로그 글을 가져오기 위해서는 쿼리셋이 필요하다.

from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect



def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # 포스트 모델에서 쿼리셋을 이용하여 날자순 필터를 이용해 글을 가져온다.
    #post는 쿼리셋의 이름이다.
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return redirect('post_detail', pk=post.pk)


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form =PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)