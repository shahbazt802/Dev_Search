from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from .models import Projects
from .forms import ProjectForm

# projectList = [{
#     'id': '1',
#     'title': 'Ecommerse Webiste',
#     'description': 'This is rendering item'
# },
#     {'id': '2',
#      'title': 'Senior Webiste',
#      'description': 'This is rendering item'
#      }, {'id': '3',
#          'title': 'Junior Webiste',
#          'description': 'This is rendering item'
#          }

# ]


def index(request):
    return HttpResponse("This is the first request")


def about(request):
    return render(request, 'index.html')


# def navbar1(request):
#     return render(request, 'navbar1.html')


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


def createProject(request):
    forms = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')

        # print(request.POST)
    context = {'form': forms}
    return render(request, 'projects/project_form.html', context)


def updateProject(request, pk):
    project = Projects.objects.get(id=pk)
    forms = ProjectForm(instance=project)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

        # print(request.POST)
    context = {'form': forms}
    return render(request, 'projects/project_form.html', context)


def deleteProject(request, pk):

    project = Projects.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'projects/delete_template.html', context)
