from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from blogapp.sitemaps import PostSitemap

sitemaps = {
    'items': PostSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogapp.urls', namespace='blogapp')),
    path('auth/', include('user.urls', namespace='user')),
    path('tinymce/', include('tinymce.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
