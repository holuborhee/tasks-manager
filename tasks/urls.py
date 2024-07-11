from django.urls import path, include
from .views import task_list_view

urlpatterns = [
    path('api/', include('tasks.api_urls')),  # Include API URLs with "api" prefix
    path('tasks/', task_list_view, name='home'),  # URL for the HTML template
]
