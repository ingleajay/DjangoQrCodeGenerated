from django.contrib import admin
from .models import UserLink
# Register your models here.


@admin.register(UserLink)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'qr_link', 'qr_title')
