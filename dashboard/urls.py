from django.urls import path
from . import views

urlpatterns = [
    path('', views.DashboardIndex.as_view(), name='dashboard-index'),
]