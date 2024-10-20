from django.http import HttpResponse


def home(request):
    return HttpResponse("Home Page")


def about(request):
    return HttpResponse("About Page")


def contact(request):
    return HttpResponse("Contact Page")
