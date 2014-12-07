from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^edit_catalog_test/', 'ifmo_catalog.views.edit_catalog'),
    url(r'^course/edit_catalog', 'ifmo_catalog.views.edit_catalog'),
    url(r'^all_courses/', 'ifmo_catalog.views.all_courses'),
    url(r'^edit_catalog_handler/', 'ifmo_catalog.views.edit_catalog_handler'),
)