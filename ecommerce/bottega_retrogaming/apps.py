from django.apps import AppConfig

class BottegaRetrogamingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bottega_retrogaming'

    def ready(self):
        from . import signals # noqa
