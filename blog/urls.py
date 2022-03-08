from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogIndex.as_view(), name='blog-index'),
    path('detail/<int:id>', views.BlogDetail.as_view(), name='blog-detail'),
    path('create/', views.BlogCreate.as_view(), name='blog-create'),
    path('update/<int:id>', views.BlogUpdate.as_view(), name='blog-update'),
    path('delete/<int:id>', views.BlogDelete.as_view(), name='blog-delete'),
]