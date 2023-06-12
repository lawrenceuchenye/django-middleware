
# Djangi middleware
class DemoMiddleware:
    # init and call are compulsory methods
    # which are to implements in every middleware
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        print("middleware running")
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print(f"Process {view_func.__name__}")
