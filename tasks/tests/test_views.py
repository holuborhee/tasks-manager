from django.test import TestCase, Client
from django.contrib.auth.models import User
from tasks.models import Task
from django.urls import reverse
import json

class GetTasksByStatusViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.task1 = Task.objects.create(
            title='Task 1',
            description='This is task 1.',
            status='in-progress',
            priority='L',
            due_date='2024-07-15 12:00:00',
            category='Work',
            assigned_to=self.user
        )
        self.task2 = Task.objects.create(
            title='Task 2',
            description='This is task 2.',
            status='completed',
            priority='M',
            due_date='2024-07-16 12:00:00',
            category='Home',
            assigned_to=self.user
        )
        self.task3 = Task.objects.create(
            title='Task 3',
            description='This is task 3.',
            status='overdue',
            priority='H',
            due_date='2024-07-14 12:00:00',
            category='Personal',
            assigned_to=self.user
        )

    def test_get_tasks_by_status_in_progress(self):
        response = self.client.get(reverse('get_tasks_by_status', args=['in-progress']))
        self.assertEqual(response.status_code, 200)
        tasks = json.loads(response.content)['tasks']
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]['title'], 'Task 1')

    def test_get_tasks_by_status_completed(self):
        response = self.client.get(reverse('get_tasks_by_status', args=['completed']))
        self.assertEqual(response.status_code, 200)
        tasks = json.loads(response.content)['tasks']
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]['title'], 'Task 2')

    def test_get_tasks_by_status_overdue(self):
        response = self.client.get(reverse('get_tasks_by_status', args=['overdue']))
        self.assertEqual(response.status_code, 200)
        tasks = json.loads(response.content)['tasks']
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]['title'], 'Task 3')

    def test_get_tasks_with_filters(self):
        response = self.client.get(reverse('get_tasks_by_status', args=['in-progress']), {
            'assigned_to': self.user.id,
            'sort_priority': 'asc',
            'search_title': 'Task 1'
        })
        self.assertEqual(response.status_code, 200)
        tasks = json.loads(response.content)['tasks']
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]['title'], 'Task 1')

    def test_get_tasks_with_sort_desc(self):
        response = self.client.get(reverse('get_tasks_by_status', args=['in-progress']), {
            'sort_priority': 'desc'
        })
        self.assertEqual(response.status_code, 200)
        tasks = json.loads(response.content)['tasks']
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]['priority'], 'L')

    def test_get_tasks_search_by_title(self):
        response = self.client.get(reverse('get_tasks_by_status', args=['in-progress']), {
            'search_title': 'Task 1'
        })
        self.assertEqual(response.status_code, 200)
        tasks = json.loads(response.content)['tasks']
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]['title'], 'Task 1')
