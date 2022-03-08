from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReportIndex.as_view(), name='report-index'),
    path('delete/<int:id>', views.ReportDelete.as_view(), name='report-delete'),
]