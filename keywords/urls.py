from django.urls import path
from . import views

urlpatterns = [
    path('', views.KeywordIndex.as_view(), name='keyword-index'),
    path('detail/<int:id>', views.KeywordDetail.as_view(), name='keyword-detail'),
    path('create/', views.KeywordCreate.as_view(), name='keyword-create'),
    path('update/<int:id>', views.KeywordUpdate.as_view(), name='keyword-update'),
    path('delete/<int:id>', views.KeywordDelete.as_view(), name='keyword-delete'),
    path('group/<int:id>', views.KeywordGroupIndex.as_view(), name='keywordgroup-index'),
    path('group-create/', views.KeywordGroupCreate.as_view(), name='keywordgroup-create'),
    path('group-detail/<int:id>', views.KeywordGroupDetail.as_view(), name='keywordgroup-detail'),
    path('group-update/<int:id>', views.KeywordGroupUpdate.as_view(), name='keywordgroup-update'),
    path('group-delete/<int:id>', views.KeywordGroupDelete.as_view(), name='keywordgroup-delete'),
]