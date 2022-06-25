from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Post


class PostCreateView(CreateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('blog: all')
    # context_object_name = 'posts'
    template_name = 'home.html'


class PostListView(ListView):
    model = Post
    # context_object_name = 'posts'
    template_name = 'list.html'


class PostDetailView(DetailView):
    model = Post
    # context_object_name = 'posts'
    template_name = 'detail.html'


class PostUpdateView(UpdateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('blog: all')
    template_name = "update.html"


class PostDeleteView(DeleteView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('blog: all')
    template_name = "update.html"
