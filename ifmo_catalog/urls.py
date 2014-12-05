from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^dashboard/edit_catalog_test', 'ifmo_catalog.views.edit_catalog'),
    url(r'^course/edit_catalog', 'ifmo_catalog.views.edit_catalog'),
    url(r'^dashboard/all_courses', 'ifmo_catalog.views.all_courses'),
    url(r'^dashboard/edit_catalog_test/delete_label/(?P<id>\d+)/$','ifmo_catalog.views.delete_label'),
)
