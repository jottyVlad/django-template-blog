from django.urls import path, include
from .views import ListPost, DetailPost

urlpatterns = [
    path('all/', ListPost.as_view(), name="list"),
    path('<int:pk>', DetailPost.as_view(), name="detail"),
]