from django.contrib import admin

# Register your models here.
from .import models
# Register your models here.
# admin.site.register(models.Carbrand)

class brandAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('Name',)}
    list_display=['Name','slug']

admin.site.register(models.Carbrand,brandAdmin)