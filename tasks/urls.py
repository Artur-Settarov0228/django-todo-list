from django.urls import path

from . views import Tasklistview, Addtasksview

urlpatterns = [
    path('/', Tasklistview.as_view(), name='task-list'),
    path('add/', Addtasksview.as_view(), name='task-add'),
]
