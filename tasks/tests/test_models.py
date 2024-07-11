from django.test import TestCase
from django.contrib.auth.models import User
from tasks.models import Task

class TaskModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.task = Task.objects.create(
            title='Test Task',
            description='This is a test task.',
            status='in-progress',
            priority='M',
            due_date='2024-07-15 12:00:00',
            category='Work',
            assigned_to=self.user
        )

    def test_task_creation(self):
        self.assertEqual(self.task.title, 'Test Task')
        self.assertEqual(self.task.description, 'This is a test task.')
        self.assertEqual(self.task.status, 'in-progress')
        self.assertEqual(self.task.priority, 'M')
        self.assertEqual(self.task.due_date, '2024-07-15 12:00:00')
        self.assertEqual(self.task.category, 'Work')
        self.assertEqual(self.task.assigned_to.username, 'testuser')

    def test_task_str_representation(self):
        self.assertEqual(str(self.task), 'Test Task')
