from django.contrib import admin
from .models import Player,Clubs

# Register your models here.



class PlayerAdmin(admin.ModelAdmin):
    readonly_fields = ("full_name",)

admin.site.register(Player,PlayerAdmin)
admin.site.register(Clubs)