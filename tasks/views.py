from django.shortcuts import render
from django.views.generic import ListView, View
from django.http import HttpRequest, HttpResponse, JsonResponse
from . models import Task

# Create your views here.

class Tasklistview(ListView):
    model = Task
    template_name = 'tasks.html'
    context_object_name = 'todos'

class Addtasksview(View):

    def post(self, request: HttpRequest) -> HttpResponse:
        title = request.POST('title')
        description = request.POST('description')
        is_completed = request.POST('is_completed')


        if not title:
            return JsonResponse({'title' : 'title required'}, status = 400)
        
        elif len(title) > 200:
            return JsonResponse({ ' title' : 'max 200'}, status = 400)
        
        if not description:
            return JsonResponse({'description': 'description required'}, status = 400)
        

        task = Task(
            title =title,
            description = description,
            is_completed = is_completed
        )
        task.save()

        return JsonResponse({'massage' : 'create tasks', 'id':task.id}, status = 201)
        



      
        
        






