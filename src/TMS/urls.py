"""TMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from tmsapp.views import home
from accounts.views import register, login_view, user_logout
from tmsapp.views import about, ActivityListView, ActivityCreateView, \
    TaskCreateView, TaskListView, AssignmentListView, AssignmentCreateView
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home),
    url(r'^register/$', register),
    url(r'^login/$', login_view),
    url(r'^logout/$', user_logout),
    url(r'^about/$', about),
    url(r'^activity/$', ActivityListView.as_view(), name='activity_list_view'),
    url(r'^activity/create/$', ActivityCreateView.as_view(), name='activity_create_view'),
    url(r'^task/create/$', TaskCreateView.as_view(), name='task_create_view'),
    url(r'^task/$', TaskListView.as_view(), name='task_list_view'),
    url(r'^assignment/$', AssignmentListView, name='assignment_list_view'),
    url(r'^assignment/create/$', AssignmentCreateView.as_view(), name='assignment_create_view'),

]
