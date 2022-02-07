from django.apps import AppConfig


class EmailNewsletterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'email_newsletter'
    verbose_name = 'Работа с новостной рассылкой'
