from django.apps import AppConfig

#chama uma aplicativo do django e inseri no settings para conseguir rodas
class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gerenciar.core'
