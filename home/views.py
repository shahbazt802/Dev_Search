from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("This is the first request")


def about(request):
    return render(request, 'projects/index.html')


def contact(request):
    return HttpResponse("Thiks is contact page")


def service(request, pk):
    return HttpResponse("Thiks is service page"+" "+str(pk))
