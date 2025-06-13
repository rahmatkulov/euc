from django.urls import path
from . import views 
app_name = "common"

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),

    path('group-list', views.GroupListView.as_view(), name='group-list'),
    path('group-create', views.GroupCreateView.as_view(), name='group-create'),
    path('group/<int:pk>/update', views.GroupUpdateView.as_view(), name='group-update'),
    path('group/<int:pk>/delete', views.GroupDeleteView.as_view(), name='group-delete'),

]
