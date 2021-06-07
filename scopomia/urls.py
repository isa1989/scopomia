from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls import handler404

# from core.views import error_404


# def response_error_handler(request, exception=None):
#     return HttpResponse('Error handler content', status=404)


# handler404 = error_404
handler404 = 'core.views.handler404'
handler500 = 'core.views.handler500'

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include("core.urls")),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += [
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
]

urlpatterns += i18n_patterns(
    path('', include("core.urls")),
    # path('accounts/', include("base_user.urls", namespace="account")),
)

if settings.PROD:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Scopomia Admin'
admin.site.site_title = 'Scopomia Administration'
admin.site.index_title = 'Scopomia Administration'
