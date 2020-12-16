from django.urls import path, include
from .views import ListPost, DetailPost

urlpatterns = [
    path('all/', ListPost.as_view(), name="list_view_posts"),
    path('<int:pk>', DetailPost.as_view(), name="list_view_posts"),
]