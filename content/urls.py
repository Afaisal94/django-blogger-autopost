from django.urls import path
from . import views

urlpatterns = [
    # CONTENT NEWS
    path('contentnews', views.ContentNewsIndex.as_view(), name='contentnews-index'),
    path('contentnews/detail/<int:id>', views.ContentNewsDetail.as_view(), name='contentnews-detail'),
    path('contentnews/delete/<int:id>', views.ContentNewsDelete.as_view(), name='contentnews-delete'),
    path('contentnews/scrape-contentnews/', views.ScrapeContentNews.as_view(), name='scrape-contentnews'),
    path('contentnews/export-contentnews/', views.ExportContentNews.as_view(), name='export-contentnews'),
    # path('import-content_news/', views.ImportContent.as_view(), name='import-content_news'),
    # CONTENT AGC
    path('contentagc', views.ContentAgcIndex.as_view(), name='contentagc-index'),
    path('contentagc/detail/<int:id>', views.ContentAgcDetail.as_view(), name='contentagc-detail'),
    path('contentagc/delete/<int:id>', views.ContentAgcDelete.as_view(), name='contentagc-delete'),
    path('contentagc/scrape-contentagc/', views.ScrapeContentAgc.as_view(), name='scrape-contentagc'),
    path('contentagc/export-contentagc/', views.ExportContentAgc.as_view(), name='export-contentagc'),
]