from django.contrib import admin
from django.urls import path, include, re_path
from users.views import discipline_list, scientist_list, state_list, student_list, tag_list
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Scientist Project API",
      default_version='v2',
      description="API documentation for Scientist Project",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/discipline_list/', discipline_list, name='discipline_list'),
    path('api/scientist_list/', scientist_list, name='scientist_list'),
    path('api/state_list/', state_list, name='state_list'),
    path('api/student_list/', student_list, name='student_list'),
    path('api/tag_list/', tag_list, name='tag_list'),
    path('api/docs/', include('rest_framework.urls')),
    re_path(r'^api/docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
