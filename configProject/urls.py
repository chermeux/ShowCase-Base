"""
Librairies
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
    path('admin/', include('admin_honeypot.urls')),
    path('secureAdmSite/', admin.site.urls),
    path('', include('show_case.urls')),
    path('partners/', include('partners.urls')),
    path('product/', include('product.urls'))

]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
