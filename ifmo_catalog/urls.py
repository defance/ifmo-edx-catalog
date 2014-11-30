from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^course/edit_catalog$', 'ifmo_catalog.views.edit_catalog'),
    url(r'^dashboard/try1', 'ifmo_catalog.views.try1'),
)
