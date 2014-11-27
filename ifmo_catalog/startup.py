from django.conf import settings
from django.conf.urls import include, url
from path import path


import edxmako


def patch_templates():
    # TODO Add template path to template look up path collection in settings
    template_path = path(__file__).dirname() / 'templates'
    edxmako.paths.add_lookup('main', template_path, prepend=True)
    if settings.SERVICE_VARIANT == 'cms':
        edxmako.paths.add_lookup('lms.main', template_path, prepend=True)


def _patch_variant_url(app_name, urls_module):
    app_urls = __import__('%s.urls' % (app_name,), fromlist=['urlpatterns'])
    app_urls.urlpatterns.insert(0, url(r'', include(urls_module)))


def patch_urls():
    try:
        _patch_variant_url('lms', 'ifmo_catalog.urls')
        _patch_variant_url('cms', 'ifmo_catalog.urls')
    except Exception:
        pass


def run():
    patch_templates()
    patch_urls()
