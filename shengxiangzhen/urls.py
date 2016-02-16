from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.contrib import admin
from products.views import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shengxiangzhen.views.home', name='home'),
    # url(r'^shengxiangzhen/', include('shengxiangzhen.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^$',main),
    (r'^brandintro/$',brandintro),
    (r'^contact/$',contact),
    url(r'^admin/', include(admin.site.urls)),
)
