from django.utils.deprecation import MiddlewareMixin


class MyMw(MiddlewareMixin):

    def process_request(self, request):
        print('MyMw process_request do--')

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('MyMw process_view do--')

    def process_response(self, request, response):
        print('MyMw process_response do--')
        return response




