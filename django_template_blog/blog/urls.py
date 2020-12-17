from django.shortcuts import redirect
from django.urls import path
from .views import ListPost, DetailPost, CreatePostView, RegistrationFormView

urlpatterns = [
    path('', lambda x: redirect('blog:list')),
    path('all/', ListPost.as_view(), name="list"),
    path('<int:pk>', DetailPost.as_view(), name="detail"),
    path('create/', CreatePostView.as_view(), name="create"),
    path('signup/', RegistrationFormView.as_view(), name="signup")
]