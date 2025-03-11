# from django.shortcuts import render

# Import necessary modules and functions
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Task

# Registration view for new users
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in immediately after registration
            return redirect('task-list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# Create your views here.

# Task List View - shows all tasks for logged-in users
class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        priority = self.request.GET.get('priority')
        if q:
            queryset = queryset.filter(title__icontains=q)
        if priority:
            queryset = queryset.filter(priority=priority)
        return queryset

# Task Create View - allows users to add a new task
class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'due_date', 'priority', 'completed']
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task-list')

# Task Update View - allows users to edit an existing task
class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'due_date', 'priority', 'completed']
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task-list')

# Task Delete View - allows users to delete a task
class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task-list')
