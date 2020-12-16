from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class ListPost(ListView):
    template_name = "blog/list.html"

    model = Post

    def get_queryset(self):
        return super(ListPost, self).get_queryset().filter(is_published=True)


class DetailPost(DetailView):
    template_name = "blog/detail.html"

    model = Post

    def get_queryset(self):
        return super(DetailPost, self).get_queryset().filter(is_published=True)
