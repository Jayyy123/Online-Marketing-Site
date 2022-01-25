from django.apps import AppConfig


class OmsaccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'omsaccount'

    def ready(self):
        import omsaccount.signals
    