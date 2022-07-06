from django.contrib import admin

from project.models import Token, Blockchain

admin.site.register(Blockchain)
admin.site.register(Token)
