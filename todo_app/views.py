from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from todo.models import Task
def home(request):
    pending_tasks=Task.objects.filter(is_complete=False).order_by("-updated_at")
    complete_tasks=Task.objects.filter(is_complete=True)
    context={
        "pending_tasks":pending_tasks,
        "complete_tasks":complete_tasks
    }
    return render(request,"home.html",context)

