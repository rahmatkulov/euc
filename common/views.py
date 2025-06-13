from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from common import forms
from . import models


from helpers.views import CreateView, UpdateView, DeleteView 


class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')

class GroupListView(ListView):
    model = models.Group
    template_name = "groups/list.html"

    context_object_name = "objects"
    queryset = model.objects.all().order_by("-id")
    paginate_by = 10

class GroupCreateView(CreateView):
    model = models.Group 
    form_class = forms.GroupForm
    template_name = "groups/create.html"
    context_object_name = "object"
    success_url = "common:group-list"
    success_create_url = "common:group-create"


class GroupUpdateView(UpdateView):
    model = models.Group
    form_class = forms.GroupForm
    template_name = "groups/update.html"
    context_object_name = "object"
    success_url = "common:group-list"
    success_update_url = "common:group-update"


class GroupDeleteView(DeleteView):
    model = models.Group
    success_url = "common:group-list"


