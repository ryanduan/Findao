from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kuiba.views.home', name='home'),
    # url(r'^kuiba/', include('kuiba.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$','manji.views.index'),
    url(r'^regist/','manji.views.regist'),
    url(r'^login/$','manji.views.login'),
    url(r'^logout/$','manji.views.logout'),
    url(r'^dispshare','manji.views.dispshare'),
)
