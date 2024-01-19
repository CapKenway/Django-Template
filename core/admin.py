from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered
from django.apps import apps
# Register your models here.

for app in apps.get_app_configs():
            if not (app.name).__contains__('django.'):
                all_models = apps.get_app_config(app.label).get_models()
                for model in all_models:
                    try:
                        admin.site.register(model)
                    except AlreadyRegistered:
                        pass