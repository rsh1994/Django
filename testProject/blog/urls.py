from django.urls import path 
from . import views 
from django.shortcuts import render

app_name = 'blog' 
urlpatterns = [ path('', views.index), ]

def index(request):
    #return HttpResponse(template.render(context, request))
    return render(request, 'blog/index.html', context)