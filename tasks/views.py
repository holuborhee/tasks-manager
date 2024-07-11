from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import Task
import json

@csrf_exempt
def create_task(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        task = Task.objects.create(
            title=data['title'],
            description=data['description'],
            status=data['status'],
            priority=data['priority'],
            due_date=data['due_date'],
            category=data['category'],
            assigned_to=User.objects.get(id=data['assigned_to'])
        )
        return JsonResponse({'message': 'Task created successfully', 'task': task.id})

@csrf_exempt
def get_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return JsonResponse({
        'title': task.title,
        'description': task.description,
        'status': task.status,
        'priority': task.priority,
        'due_date': task.due_date,
        'category': task.category,
        'assigned_to': task.assigned_to.id
    })

@csrf_exempt
def update_task(request, task_id):
    if request.method == 'PUT':
        data = json.loads(request.body)
        task = get_object_or_404(Task, id=task_id)
        task.title = data['title']
        task.description = data['description']
        task.status = data['status']
        task.priority = data['priority']
        task.due_date = data['due_date']
        task.category = data['category']
        task.assigned_to = User.objects.get(id=data['assigned_to'])
        task.save()
        return JsonResponse({'message': 'Task updated successfully'})

@csrf_exempt
def delete_task(request, task_id):
    if request.method == 'DELETE':
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        return JsonResponse({'message': 'Task deleted successfully'})

@csrf_exempt
def get_tasks_by_status(request, status):
    status_map = {
        'in-progress': 'IP',
        'completed': 'CO',
        'overdue': 'OV'
    }
    
    if status not in status_map:
        return JsonResponse({'error': 'Invalid status'}, status=400)
    
    # Fetch query parameters
    assigned_to = request.GET.get('assigned_to')
    sort_priority = request.GET.get('sort_priority')
    search_title = request.GET.get('search_title')
    
    tasks = Task.objects.filter(status=status_map[status])

    # Filter by assigned_to if provided
    if assigned_to:
        tasks = tasks.filter(assigned_to__id=assigned_to)

    # Search by task title if provided
    if search_title:
        tasks = tasks.filter(title__icontains=search_title)

    # Priority mapping for sorting
    priority_mapping = {'L': 1, 'M': 2, 'H': 3}

    # Custom sort by priority if provided
    if sort_priority:
        reverse = sort_priority.lower() == 'desc'
        tasks = sorted(tasks, key=lambda task: priority_mapping[task.priority], reverse=reverse)

    tasks_data = [
        {
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'status': task.status,
            'priority': task.priority,
            'due_date': task.due_date,
            'category': task.category,
            'assigned_to': task.assigned_to.id
        }
        for task in tasks
    ]
    return JsonResponse({'tasks': tasks_data})

def task_list_view(request):
    return render(request, 'dashboard.html')

def get_users(request):
    users = User.objects.all()
    users_data = [{'id': user.id, 'username': user.username} for user in users]
    return JsonResponse({'users': users_data})

