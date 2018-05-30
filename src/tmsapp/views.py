from django.shortcuts import render
from .forms import ActivityForm, TaskForm, AssignmentForm
# Create your views here.

from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.contrib.messages.views import SuccessMessageMixin

from django.views.generic.base import TemplateView, TemplateResponseMixin, ContextMixin
from django.http import HttpResponse, Http404
from django.views.generic import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView, MultipleObjectMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView, ModelFormMixin
from .models import Activity, Task, Assignment


def home(request):
    return render(request, 'base.html', {})


def about(request):
    form = ActivityForm(request.POST or None)

    return render(request, 'activity.html', {'form': form})


class ActivityListView(ListView):
    model = Activity
    template_name = 'activity_list.html'

    def get_queryset(self, *args, **kwargs):
        qs = super(ActivityListView, self).get_queryset(*args, **kwargs)

        return qs


class ActivityCreateView(SuccessMessageMixin, CreateView):
    # model = Book
    template_name = 'activity_create.html'
    # fields = ['title', 'description']
    form_class = ActivityForm

    def get_success_url(self):
        return reverse('activity_create_view')


class TaskCreateView(SuccessMessageMixin, CreateView):
    # model = Book
    template_name = 'task_create.html'
    # fields = ['title', 'description']
    form_class = TaskForm

    # success_message = "%(title)s has been created"

    def get_success_url(self):
        return reverse('task_create_view')


class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'

    def get_queryset(self, *args, **kwargs):
        qs = super(TaskListView, self).get_queryset(*args, **kwargs)
        print(qs)
        return qs


def AssignmentListView(request):
    template_name = 'assignment_list.html'
    task = Task.objects.all()
    assignment = Assignment.objects.all()

    context = {
        'task': task,
        'assignment': assignment
    }

    return render(request, template_name, context)


class AssignmentCreateView(SuccessMessageMixin, CreateView):
    template_name = 'assignment_create.html'
    form_class = AssignmentForm

    def get_success_url(self):
        return reverse('assignment_create_view')
