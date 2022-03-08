from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('mail/', include('mail.urls')),
    path('blog/', include('blog.urls')),
    path('keyword/', include('keywords.urls')),
    path('content/', include('content.urls')),
    path('campaign/', include('campaign.urls')),
    path('report/', include('report.urls'))
]
