from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.

class PostList(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.order_by('-created')


class PostDetail(DetailView):
    model = Post

# def detail(request, pk):
#     post = Post.objects.get(pk=pk)
#     context{'object':post, 'post':post}
#     return render(request, 'blog/post_detail.html', {'object':post})

# def index(request):
#     object_list = Post.objects.all()
#     context = {'object_list':object_list}
#     return render(request, 'blog/post_list.html', context)

