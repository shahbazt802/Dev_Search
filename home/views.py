from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("This is the first request")


def about(request):
    return render(request, 'index.html')


def projects(request):
    msg = "projects"
    return render(request, 'projects/projects.html', {'msg': msg})


def contact(request):
    return render(request, 'projects/navbar.html')


def service(request, pk):
    return HttpResponse("Thiks is service page"+" "+str(pk))
