from django.contrib import admin
from .models import Client, Pregnancy, PregnancyEvent

# Register your models here.

admin.site.register(Client)
admin.site.register(Pregnancy)
admin.site.register(PregnancyEvent)