from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, FormView, UpdateView
from django.views.generic.edit import FormMixin, DeleteView

from .forms import CreatePostForm, CreateComment
from .models import Post, Comment


class ListPost(ListView):
    paginate_by = 5
    template_name = "blog/list.html"

    model = Post

    def get_queryset(self):
        if not self.request.user.is_superuser:
            return super(ListPost, self).get_queryset().filter(is_published=True).order_by('-created_at')
        else:
            return super(ListPost, self).get_queryset().order_by('-created_at')


class DetailPost(FormMixin, DetailView):
    template_name = "blog/detail.html"
    model = Post
    form_class = CreateComment

    def get_queryset(self):
        if not self.request.user.is_superuser:
            return super(DetailPost, self).get_queryset().filter(is_published=True)
        else:
            return super(DetailPost, self).get_queryset()

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['comments'] = Comment.objects.filter(post=kwargs['object'].id).order_by('-created_at')
        data['is_authed'] = self.request.user.is_authenticated
        if (self.request.user == (self.get_object()).author) or self.request.user.is_superuser:
            data['is_access'] = True
        else:
            data['is_access'] = False

        data['form'] = self.get_form()
        return data

    def get(self, request, *args, **kwargs):
        post_object = self.get_object()
        post_object.views += 1
        post_object.save()
        return super().get(request, *args, **kwargs)

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
                          post=self.get_object(),
                          text=text)
        comment.save()
        post_object = self.get_object()
        post_object.views -= 1
        post_object.save()

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


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'blog/update.html'
    template_name_suffix = '_update_post_form'
    form_class = CreatePostForm

    def get(self, *args, **kwargs):
        if (self.request.user != (self.get_object()).author) and (not self.request.user.is_superuser):
            return redirect('blog:detail', self.kwargs['pk'])

        return super().get(*args, **kwargs)


class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete.html'
    success_url = '/all'

    def get(self, *args, **kwargs):
        print(self.request.user != self.get_object().author)
        if (self.request.user != (self.get_object()).author) and (not self.request.user.is_superuser):
            return redirect('blog:detail', self.kwargs['pk'])

        return super().get(*args, **kwargs)


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
