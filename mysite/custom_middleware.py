from django.utils.deprecation import MiddlewareMixin


class CustomMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        print('calling process request ')
        return None

    def process_response(self, request, response):
        response['X-Developer'] = 'remote Python developers'
        return response