from .models import UserStat

# Djangi middleware


class DemoMiddleware:
    # init and call are compulsory methods
    # which are to implements in every middleware
    def __init__(self, get_response):
        self.get_response = get_response

    def os_stats_update(self, os_info):
        stats = UserStat.objects.get(id=1)
        if "Android" in os_info:
            stats.android += 1
            stats.save()
        if "x86_64" in os_info:
            stats.desktop += 1
            stats.save()

    def __call__(self, request):
        self.os_stats_update(request.META["HTTP_USER_AGENT"])
        response = self.get_response(request)
        print("middleware running")
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print(f"Process {view_func.__name__}")

    def process_exception(self, request, exception):
        pass
