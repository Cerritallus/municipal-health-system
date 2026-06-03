from django.http import HttpResponseForbidden

class HoneypotMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if request.method == "POST":

            if request.POST.get("phone_number"):
                return HttpResponseForbidden("Bot detected")

        return self.get_response(request)