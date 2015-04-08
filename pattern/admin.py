from django.contrib import admin
from pattern.models import *

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
	list_display = ('unique_id', 'name', 'desc', 'image_url')

admin.site.register(Item, ItemAdmin)