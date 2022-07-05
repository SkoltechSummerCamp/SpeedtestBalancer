import os

from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Balancer API",
      default_version='0.1.0',
      description="Speedtest load balancer",
      contact=openapi.Contact(email=os.environ["SUPPORT_EMAIL"]),
      license=openapi.License(name="Apache 2.0", url='https://www.apache.org/licenses/LICENSE-2.0.html'),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui()),
    path('', include('services.urls')),
]
