from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Teacher, Lesson
from .serializers import TeacherSerializer, LessonSerializer, ResultsSetPagination


class SingleTeacherView(RetrieveAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class AllTeachersView(ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    pagination_class = ResultsSetPagination


class TeacherLessonsView(ListAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Lesson.objects.filter(teacher__pk=pk)
