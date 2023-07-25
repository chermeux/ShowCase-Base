"""
Librairies
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', include('admin_honeypot.urls')),
    path('secureAdmSite/', admin.site.urls),
    path('', include('ShowCase.urls'))

]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
