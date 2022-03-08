from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContentIndex.as_view(), name='content-index'),
    path('detail/<int:id>', views.ContentDetail.as_view(), name='content-detail'),
    path('delete/<int:id>', views.ContentDelete.as_view(), name='content-delete'),
    path('scrape-content/', views.ScrapeContent.as_view(), name='scrape-content'),
    path('import-content/', views.ImportContent.as_view(), name='import-content'),
]