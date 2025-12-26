from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django running in Kubernetes!")

def health(request):
    return HttpResponse("OK")