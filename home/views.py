from django.shortcuts import render, HttpResponse

# Create your views here.
from .models import Projects

projectList = [{
    'id': '1',
    'title': 'Ecommerse Webiste',
    'description': 'This is rendering item'
},
    {'id': '2',
     'title': 'Senior Webiste',
     'description': 'This is rendering item'
     }, {'id': '3',
         'title': 'Junior Webiste',
         'description': 'This is rendering item'
         }

]


def index(request):
    return HttpResponse("This is the first request")


def about(request):
    return render(request, 'index.html')


def projects(request):
    msg = "projects"
    projects = Projects.objects.all()
    context = {'msg': msg, 'projects': projects}
    return render(request, 'projects/projects.html', context)


def project(request, pk):

    projectObj = Projects.objects.get(id=pk)
    # tags = projectObj.tag.all()

    return render(request, 'projects/navbar.html', {'projectobj': projectObj})


def service(request, pk):
    return HttpResponse("Thiks is service page"+" "+str(pk))
