from django.shortcuts import render

def index(request):
    context = {}
    return render(request,'polls/index.html',context)
def projects(request):
    context={}
    return render(request,'polls/projects.html',context)
def languages(request):
    context={}
    return render(request,'polls/languages.html',context)
