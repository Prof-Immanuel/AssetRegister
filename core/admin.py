from django.contrib import admin
from .models import StolenItem, CustomUser, Item

# Register your models here.
admin.site.register(StolenItem)
admin.site.register(CustomUser)
admin.site.register(Item)