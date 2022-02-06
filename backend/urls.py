from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="MyLiving Backend API",
      default_version='v1',
      description="Docs for the Backend API, check periodically for additions.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="jimmywilliamotieno@gmail.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('housing/', include('housing.urls', namespace='housing'))
]
