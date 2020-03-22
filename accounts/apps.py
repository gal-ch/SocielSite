from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        try:
            import accounts.signals
            from .signals import user_signed_up
        except ImportError:
            pass