from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from drf_yasg import openapi
from rest_framework import permissions
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('Blogs/', include('NewsApp.urls'), name="blogs_app"),
    path('Quiz/', include('QuizApp.urls'), name="quiz_app"),
    path('Teachers/', include('TeacherApp.urls'), name='teachers_app'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name="swagger"),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name="redoc"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
