
# Djangi middleware
class DemoMiddleware:
    # init and call are compulsory methods
    # which are to implements in every middleware
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(request.path)
        print(request.headers["Host"])
        print(request.headers["Accept-Language"])
        print(request.META["REQUEST_METHOD"])
        print(request.META["HTTP_USER_AGENT"])
        response = self.get_response(request)
        print("middleware running")
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print(f"Process {view_func.__name__}")

    def process_exception(self, request, exception):
        pass
