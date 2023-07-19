from django.urls import path
from .views import AllTeachersView, SingleTeacherView, TeacherLessonsView

urlpatterns = [
    path('all/', AllTeachersView.as_view(), name='all_blogs'),
    path('teacher/<int:pk>/', SingleTeacherView.as_view(), name='single_blog'),
    path('teacher/<int:pk>/lessons/', TeacherLessonsView.as_view(), name='lessons')
]
