from django.test import TestCase

# Create your tests here.
import datetime
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Task

class TaskModelTest(TestCase):
    def test_string_representation(self):
        task = Task(title="Test Task")
        self.assertEqual(str(task), "Test Task")

    def test_priority_display(self):
        task = Task.objects.create(title="Test Task", priority='H')
        # Assuming 'H' corresponds to "High"
        self.assertEqual(task.get_priority_display(), "High")

class TaskViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        # Create two tasks with different priorities
        self.task1 = Task.objects.create(
            title="Task 1", 
            description="First task", 
            completed=False, 
            priority='M', 
            due_date=datetime.date.today()
        )
        self.task2 = Task.objects.create(
            title="Task 2", 
            description="Second task", 
            completed=True, 
            priority='H', 
            due_date=datetime.date.today()
        )

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('task-list'))
        login_url = reverse('login') + "?next=" + reverse('task-list')
        self.assertRedirects(response, login_url)

    def test_task_list_view_logged_in(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('task-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Task 1")
        self.assertContains(response, "Task 2")

    def test_task_filtering_by_priority(self):
        self.client.login(username='testuser', password='testpass')
        # Filter by Medium priority ('M')
        response = self.client.get(reverse('task-list') + '?priority=M')
        self.assertContains(response, "Task 1")
        self.assertNotContains(response, "Task 2")

    def test_task_create_view(self):
        self.client.login(username='testuser', password='testpass')
        new_task_data = {
            'title': 'New Task',
            'description': 'New task description',
            'completed': False,
            'priority': 'L',  # Assume 'L' is Low priority
            'due_date': datetime.date.today()
        }
        response = self.client.post(reverse('task-add'), new_task_data)
        self.assertRedirects(response, reverse('task-list'))
        self.assertTrue(Task.objects.filter(title='New Task').exists())

    def test_task_update_view(self):
        self.client.login(username='testuser', password='testpass')
        update_url = reverse('task-edit', kwargs={'pk': self.task1.pk})
        updated_data = {
            'title': 'Task 1 Updated',
            'description': self.task1.description,
            'completed': self.task1.completed,
            'priority': self.task1.priority,
            'due_date': self.task1.due_date
        }
        response = self.client.post(update_url, updated_data)
        self.assertRedirects(response, reverse('task-list'))
        self.task1.refresh_from_db()
        self.assertEqual(self.task1.title, 'Task 1 Updated')

    def test_task_delete_view(self):
        self.client.login(username='testuser', password='testpass')
        delete_url = reverse('task-delete', kwargs={'pk': self.task1.pk})
        response = self.client.post(delete_url)
        self.assertRedirects(response, reverse('task-list'))
        self.assertFalse(Task.objects.filter(pk=self.task1.pk).exists())

class RegistrationViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_registration_view_get(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Register")

    def test_registration_view_post(self):
        registration_data = {
            'username': 'newuser',
            'password1': 'complexpassword123',
            'password2': 'complexpassword123'
        }
        response = self.client.post(reverse('register'), registration_data)
        self.assertRedirects(response, reverse('task-list'))
        self.assertTrue(User.objects.filter(username='newuser').exists())
