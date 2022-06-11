from django.shortcuts import render
from project.models import Project
from blog.models import Post

def base(request):
    return render(request, "base.html")

def main(request):
    projects = Project.objects.all()
    posts = Post.objects.all()
    context = {'projects': projects, 'posts': posts}
    return render(request, 'main.html', context)