from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from drf_yasg import openapi
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg.generators import OpenAPISchemaGenerator


schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
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
                  path("ckeditor", include("ckeditor_uploader.urls")),
                  path('api/', include('NewsApp.urls')),
                  path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
