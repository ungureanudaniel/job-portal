from django.apps import apps
from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered
# from .models import ServicePost, Category, Tag, Review

app_models = apps.get_app_config('services').get_models()
# print(app_models)
for model in app_models:
    print(model)
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass
