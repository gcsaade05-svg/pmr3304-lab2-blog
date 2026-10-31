from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic

from .models import Post, Comment
from .forms import PostForm, CommentForm


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


def create_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_author = form.cleaned_data['author']
            comment_text = form.cleaned_data['text']
            comment = Comment(author=comment_author,
                              text=comment_text,
                              post=post)
            comment.save()
            return HttpResponseRedirect(
                reverse('blog:detail', args=(post_id, )))
    else:
        form = CommentForm()
    context = {'form': form, 'post': post}
    return render(request, 'blog/comment.html', context)
