from django import forms

from .models import Post, Comment


class CreatePostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Post
        fields = ['title', 'content', 'category']


class CreateComment(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['rows'] = '1'
            visible.field.widget.attrs['style'] = 'resize: vertical'

    class Meta:
        model = Comment
        fields = ['text', ]
