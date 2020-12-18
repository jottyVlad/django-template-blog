from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import FormMixin

from .forms import CreatePostForm, CreateComment
from .models import Post, Comment


class ListPost(ListView):
    paginate_by = 5
    template_name = "blog/list.html"

    model = Post

    def get_queryset(self):
        return super(ListPost, self).get_queryset().filter(is_published=True)


class DetailPost(FormMixin, DetailView):

    template_name = "blog/detail.html"
    model = Post
    form_class = CreateComment

    def get_queryset(self):
        return super(DetailPost, self).get_queryset().filter(is_published=True)
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['comments'] = Comment.objects.filter(post=kwargs['object'].id).order_by('-created_at')
        data['is_authed'] = self.request.user.is_authenticated

        data['form'] = self.get_form()
        return data

    def post(self, request, *args, **kwargs):

        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            return redirect('blog:detail', self.kwargs['pk'])

        text = form.cleaned_data.get('text')
        comment = Comment(author=self.request.user,
                          post=Post.objects.get(id=self.kwargs['pk']),
                          text=text)
        comment.save()
        return redirect('blog:detail', self.kwargs['pk'])


class CreatePostView(FormView):
    template_name = 'blog/create.html'
    form_class = CreatePostForm
    success_url = '/all'

    def form_valid(self, form):
        post = form.save()
        post.is_published = True
        post.author = self.request.user
        post.save()
        return super().form_valid(form)


class RegistrationFormView(FormView):

    template_name = 'blog/signup.html'
    form_class = UserCreationForm
    success_url = '/'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('blog:list')
        else:
            return super().get(request, *args, **kwargs)


    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return redirect('blog:list')
