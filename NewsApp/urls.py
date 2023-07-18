from django.urls import path
from .views import AllBlogsView, SingleBlogView

urlpatterns = [
    path('all/', AllBlogsView.as_view(), name='all_blogs'),
    path('blog/<int:pk>/', SingleBlogView.as_view(), name='single_blog'),
]
