from django.urls import path
from . import views

urlpatterns = [
    path('', views.KeywordIndex.as_view(), name='keyword-index'),
    path('detail/<int:id>', views.KeywordDetail.as_view(), name='keyword-detail'),
    path('create/', views.KeywordCreate.as_view(), name='keyword-create'),
    path('update/<int:id>', views.KeywordUpdate.as_view(), name='keyword-update'),
    path('delete/<int:id>', views.KeywordDelete.as_view(), name='keyword-delete'),
]