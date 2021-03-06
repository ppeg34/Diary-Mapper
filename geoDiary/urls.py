from django.conf.urls import patterns, include, url
from django.contrib.gis import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'geoDiary.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^pointDiary/', include('pointDiary.urls', namespace="pointDiary")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.simple.urls')),
)
