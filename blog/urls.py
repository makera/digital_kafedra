from django.urls import path
from blog.views import BlogView, BlogSingleView

urlpatterns = [
    path('', BlogView.as_view()),
    path('<int:pk>/', BlogSingleView.as_view()),
]
