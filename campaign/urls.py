from django.urls import path
from . import views

urlpatterns = [
    path('', views.CampaignIndex.as_view(), name='campaign-index'),
    path('detail/<int:id>', views.CampaignDetail.as_view(), name='campaign-detail'),
    path('create/', views.CampaignCreate.as_view(), name='campaign-create'),
    path('update/<int:id>', views.CampaignUpdate.as_view(), name='campaign-update'),
    path('delete/<int:id>', views.CampaignDelete.as_view(), name='campaign-delete'),
    path('run/<int:id>', views.CampaignRun.as_view(), name='campaign-run'),
]