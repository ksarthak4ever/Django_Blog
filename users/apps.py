from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self): #method just to import the signals
    	import users.signals