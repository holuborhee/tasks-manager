from django.urls import path
from .views import create_task, get_task, update_task, delete_task, get_tasks_by_status, get_users

urlpatterns = [
    path('tasks/', create_task, name='create_task'),
    path('tasks/<int:task_id>/', get_task, name='get_task'),
    path('tasks/<int:task_id>/update/', update_task, name='update_task'),
    path('tasks/<int:task_id>/delete/', delete_task, name='delete_task'),
    path('tasks/status/<str:status>/', get_tasks_by_status, name='get_tasks_by_status'),
    path('users/', get_users, name='get_users'),
]
