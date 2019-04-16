from django import template
from django.conf import settings
register = template.Library()


@register.filter
def sort_apps(apps):
    count = len(apps)
    print(f'count del index admin page: {count}')
    apps.sort(
        key=lambda x:
            settings.APP_ORDER.index(x['app_label'])
            if x['app_label'] in settings.APP_ORDER
            else count
    )
    return apps


@register.filter
def sort_models(models):
    count = len(models)
    print(f'count del index admin page models: {count}')
    name = models[0]['object_name']
    # print(f'modelo nombre: {name}')
    # print(f'settings: {settings.MODELS_ORDER.index(name)}')
    models.sort(
        key=lambda x:
            settings.MODELS_ORDER.index(x['object_name'])
            if x['object_name'] in settings.APP_ORDER
            else count
    )
    return models
