from django.urls import path
from . import views 
app_name = "common"

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    # group
    path('group-list', views.GroupListView.as_view(), name='group-list'),
    path('group-create', views.GroupCreateView.as_view(), name='group-create'),
    path('group/<int:pk>/update', views.GroupUpdateView.as_view(), name='group-update'),
    path('group/<int:pk>/delete', views.GroupDeleteView.as_view(), name='group-delete'),
    # detail group
    path('group/<str:slug>/detail', views.GroupDetailView.as_view(), name='group-detail'),


    # group-categories
    path('group-category-list', views.GroupCategoryListView.as_view(), name='group-category-list'),
    path('group-category-create', views.GroupCategoryCreateView.as_view(), name='group-category-create'),
    path('group-category/<int:pk>/update', views.GroupCategoryUpdateView.as_view(), name='group-category-update'),
    path('group-category/<int:pk>/delete', views.GroupCategoryDeleteView.as_view(), name='group-category-delete'),

    # teacher
    path('teacher-list', views.TeacherListView.as_view(), name='teacher-list'),
    path('teacher-create', views.TeacherCreateView.as_view(), name='teacher-create'),
    path('teacher/<int:pk>/update', views.TeacherUpdateView.as_view(), name='teacher-update'),
    path('teacher/<int:pk>/delete', views.TeacherDeleteView.as_view(), name='teacher-delete'),
    
    # student
    path('student-list', views.StudentListView.as_view(), name='student-list'),
    path('student-create', views.StudentCreateView.as_view(), name='student-create'),
    path('student/<int:pk>/update', views.StudentUpdateView.as_view(), name='student-update'),
    path('student/<int:pk>/delete', views.StudentDeleteView.as_view(), name='student-delete'),

    # payments
    path('payment-list', views.PaymentListView.as_view(), name='payment-list'),
    path('payment-create', views.PaymentCreateView.as_view(), name='payment-create'),
    path('payment/<int:pk>/update', views.PaymentUpdateView.as_view(), name='payment-update'),
    path('payment/<int:pk>/delete', views.PaymentDeleteView.as_view(), name='payment-delete'),
]
