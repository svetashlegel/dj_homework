from django.conf import settings
from django.core.cache import cache

from catalog.models import Category


def get_categories_cache():
    if settings.CACHE_ENABLED:
        key = 'category_list'
        category_list = cache.get(key)
        if category_list is None:
            category_list = Category.objects.all()
            cache.set(key, category_list)
    else:
        category_list = Category.objects.all()
    return category_list


def get_active_versions(obj):
    versions = obj.version_set.all()
    active_versions = []
    for version in versions:
        if version.status:
            active_versions.append(version)
    return active_versions
