from django.contrib import admin
from main.models import ContacTT
# Register your models here.
class ContacTTAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "address", "message", "sent_at")
admin.site.register(ContacTT, ContacTTAdmin)