from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView
from django.db.models import Count

from common import forms
from . import models


from helpers.views import CreateView, UpdateView, DeleteView


# HomeView
class HomeView(View):
    def get(self, request):
        return render(request, "index.html")


# views for Groups
class GroupListView(ListView):
    model = models.Group
    template_name = "groups/list.html"

    context_object_name = "objects"
    queryset = (
        models.Group.objects.all()
        .annotate(students_count=Count("students"))
        .order_by("-id")
    )
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


# DetailView for Group
class GroupDetailView(DetailView):
    model = models.Group
    template_name = "groups/detail.html"
    context_object_name = "group"


# views for GroupCategories
class GroupCategoryListView(ListView):
    model = models.GroupCategory
    template_name = "group_categories/list.html"

    context_object_name = "objects"
    queryset = (
        model.objects.all().annotate(groups_count=Count("category")).order_by("-id")
    )
    paginate_by = 10


class GroupCategoryCreateView(CreateView):
    model = models.GroupCategory
    form_class = forms.GroupCategoryForm
    template_name = "group_categories/create.html"
    context_object_name = "object"
    success_url = "common:group-category-list"
    success_create_url = "common:group-category-create"


class GroupCategoryUpdateView(UpdateView):
    model = models.GroupCategory
    form_class = forms.GroupCategoryForm
    template_name = "group_categories/update.html"
    context_object_name = "object"
    success_url = "common:group-category-list"
    success_update_url = "common:group-category-update"


class GroupCategoryDeleteView(DeleteView):
    model = models.GroupCategory
    success_url = "common:group-category-list"


# views for Teacher model
class TeacherListView(ListView):
    model = models.Teacher
    template_name = "teachers/list.html"

    context_object_name = "objects"
    queryset = models.Teacher.objects.all().order_by("-id")
    paginate_by = 10


class TeacherCreateView(CreateView):
    model = models.Teacher
    form_class = forms.TeacherForm
    template_name = "teachers/create.html"
    context_object_name = "object"
    success_url = "common:teacher-list"
    success_create_url = "common:teacher-create"


class TeacherUpdateView(UpdateView):
    model = models.Teacher
    form_class = forms.TeacherForm
    template_name = "teachers/update.html"
    context_object_name = "object"
    success_url = "common:teacher-list"
    success_update_url = "common:teacher-update"


class TeacherDeleteView(DeleteView):
    model = models.Teacher
    success_url = "common:teacher-list"


# views for Student model
class StudentListView(ListView):
    model = models.Student
    template_name = "students/list.html"

    context_object_name = "objects"
    queryset = models.Student.objects.all().order_by("-id")
    paginate_by = 10


class StudentCreateView(CreateView):
    model = models.Student
    form_class = forms.StudentForm
    template_name = "students/create.html"
    context_object_name = "object"
    success_url = "common:student-list"
    success_create_url = "common:student-create"


class StudentUpdateView(UpdateView):
    model = models.Student
    form_class = forms.StudentForm
    template_name = "students/update.html"
    context_object_name = "object"
    success_url = "common:student-list"
    success_update_url = "common:student-update"


class StudentDeleteView(DeleteView):
    model = models.Student
    success_url = "common:student-list"


# views for Payment model
class PaymentListView(ListView):
    model = models.Payment
    template_name = "payments/list.html"

    context_object_name = "objects"
    queryset = models.Payment.objects.all().order_by("-id")
    paginate_by = 10


class PaymentCreateView(CreateView):
    model = models.Payment
    form_class = forms.PaymentForm
    template_name = "payments/create.html"
    context_object_name = "object"
    success_url = "common:payment-list"
    success_create_url = "common:payment-create"


class PaymentUpdateView(UpdateView):
    model = models.Payment
    form_class = forms.PaymentForm
    template_name = "payments/update.html"
    context_object_name = "object"
    success_url = "common:payment-list"
    success_update_url = "common:payment-update"


class PaymentDeleteView(DeleteView):
    model = models.Payment
    success_url = "common:payment-list"
