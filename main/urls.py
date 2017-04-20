import os

from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from django.views.static import serve

urlpatterns = [
    url(r'^', include('partidas.urls', namespace='partidas')),
    url(r'^usuario/', include('contas.urls', namespace='contas')),
    url(r'^apostas/', include('apostas.urls', namespace='apostas')),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns.extend([
        url(
            r'^docs/(?P<path>.*)$', serve,
            {'document_root': os.path.join(settings.DOCS_ROOT, 'build/html/'),
             'show_indexes': False}
        ),
        url(
            r'^static/(?P<path>.*)$', serve,
            {'document_root': os.path.join(settings.STATIC_ROOT),
             'show_indexes': False}
        )
    ])
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns