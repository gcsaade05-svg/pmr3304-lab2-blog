from django.urls import reverse_lazy
from django.views import generic

from .models import Post
from .forms import PostForm


class PostListView(generic.ListView):
    model = Post
    template_name = 'blog/index.html'


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'


class PostCreateView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/create.html'
    success_url = reverse_lazy('blog:index')


class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/update.html'
    success_url = reverse_lazy('blog:index')


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/delete.html'
    success_url = reverse_lazy('blog:index')
