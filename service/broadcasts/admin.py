from django.contrib import admin

from broadcasts.models import Client, Broadcast, Message

admin.site.register(Client)
admin.site.register(Broadcast)
admin.site.register(Message)