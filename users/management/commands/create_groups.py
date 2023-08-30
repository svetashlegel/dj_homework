from django.core.management import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):

    def handle(self, *args, **options):
        moderator = Group.objects.create(name='Moderator')
        content_manager = Group.objects.create(name='Content_manager')
        service_user = Group.objects.create(name='Service_user')

        change_category = Permission.objects.get(codename='change_category')
        view_category = Permission.objects.get(codename='view_category')
        add_product = Permission.objects.get(codename='add_product')
        change_product = Permission.objects.get(codename='change_product')
        view_product = Permission.objects.get(codename='view_product')
        delete_product = Permission.objects.get(codename='delete_product')
        set_published = Permission.objects.get(codename='set_published')
        add_article = Permission.objects.get(codename='add_article')
        change_article = Permission.objects.get(codename='change_article')
        delete_article = Permission.objects.get(codename='delete_article')
        view_article = Permission.objects.get(codename='view_article')
        add_version = Permission.objects.get(codename='add_version')
        change_version = Permission.objects.get(codename='change_version')
        view_version = Permission.objects.get(codename='view_version')
        delete_version = Permission.objects.get(codename='delete_version')

        moderator_perm_list = [change_category, view_category, change_product, view_product, set_published]
        content_manager_perm_list = [add_article, change_article, view_article, delete_article, view_product]
        service_user_perm_list = [add_product, change_product, view_product, delete_product, set_published, add_version,
                                  change_version, view_version, delete_version, view_article]

        moderator.permissions.set(moderator_perm_list)
        content_manager.permissions.set(content_manager_perm_list)
        service_user.permissions.set(service_user_perm_list)
