from django.urls import path
from . import views

urlpatterns = [
    path('', views.MailIndex.as_view(), name='mail-index'),
    path('detail/<int:id>', views.MailDetail.as_view(), name='mail-detail'),
    path('create/', views.MailCreate.as_view(), name='mail-create'),
    path('update/<int:id>', views.MailUpdate.as_view(), name='mail-update'),
    path('delete/<int:id>', views.MailDelete.as_view(), name='mail-delete'),
]