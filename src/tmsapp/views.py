from django.shortcuts import render
from .forms import ActivityForm, TaskForm
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
from .models import Activity, Task




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
    success_message = "%(title)s has been created"

    # def form_valid(self, form):
    #     form.instance.added_by = self.request.user
    #     form.instance.last_edited_by = self.request.user
    #     valid_form = super(BookCreateView, self).form_valid(form)
    #     # messages.success(self.request, 'Book Created')
    #     return valid_form

    def get_success_url(self):
        return reverse('activity_create_view')


class TaskCreateView(SuccessMessageMixin, CreateView):
    # model = Book
    template_name = 'task_create.html'
    # fields = ['title', 'description']
    form_class = TaskForm
    success_message = "%(title)s has been created"

    def get_success_url(self):
        return reverse('task_create_view')
