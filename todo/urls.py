from django.urls import path,include
from . import views

urlpatterns = [
    path("addTask/",views.addTask,name="addTask"),
    
    # mark as done
    
    path("mark_as_Done/<int:pk>",views.mark_as_Done,name="mark_as_Done"),
    
    # mark as pending
    
    path("mark_as_pending/<int:pk>",views.mark_as_pending,name="mark_as_pending"),
    
    # edit the task
    path("edit_task/<int:pk>",views.edit_task,name="edit_task"),
    
    # delete the task
    path("delete_task/<int:pk>",views.delete_task,name="delete_task")
]