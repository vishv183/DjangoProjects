from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions, authentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from drf_yasg.inspectors import SwaggerAutoSchema

class CustomSwaggerAutoSchema(SwaggerAutoSchema):
    def get_security(self):
        return [{
            'BasicAuth': [],
            'Bearer': [],
            'OAuth2': [],
        }]

schema_view = get_schema_view(
    openapi.Info(
        title="My Site API",
        default_version='v1',
        description="Mysite API documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=[
        authentication.BasicAuthentication,
        authentication.SessionAuthentication,
        JWTAuthentication,
        OAuth2Authentication,
    ],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),  # Includes the DRF login/logout views
    path('accounts/', include('django.contrib.auth.urls')),  # Includes the Django auth URLs
    path('api/', include('Profile.urls')),
    path('laptop/', include('laptop.urls')),
    path('watch/', include('Watches.urls')),
    path('testing/', include('sampleapp.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
