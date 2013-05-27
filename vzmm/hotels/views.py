

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Welcome to Hotels. You're at the hotels index.")


