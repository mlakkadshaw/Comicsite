from django.conf.urls.defaults import patterns, include, url
from comics.comic.views import add_comic, display_comic
import settings
from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': settings.MEDIA_ROOT}),
    # Examples:
    # url(r'^$', 'comics.views.home', name='home'),
    # url(r'^comics/', include('comics.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comics/(\d{1,2})/$',display_comic),
    url(r'^comics/$',display_comic),
    url(r'^$',display_comic),
    url(r'^comics/add/$',add_comic),
    url(r'^accounts/login/$',login),
    url(r'^accounts/logout/$',logout),
)
