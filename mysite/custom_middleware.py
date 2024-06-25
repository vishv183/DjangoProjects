from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from Profile.utils import can_access_swagger


class SwaggerAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        swagger_paths = [
            reverse('schema-swagger-ui'),
            reverse('schema-json', kwargs={'format': '.json'}),
            reverse('schema-json', kwargs={'format': '.yaml'}),
            reverse('schema-redoc')
        ]
        if any(request.path.startswith(path) for path in swagger_paths):
            if not can_access_swagger(request.user):
                return redirect(f"{settings.LOGIN_URL}?next={request.path}")
        response = self.get_response(request)
        return response
