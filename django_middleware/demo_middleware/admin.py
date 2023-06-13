from django.contrib import admin
from .models import UserStat

# Register your models here.


@admin.register(UserStat)
class UserStats(admin.ModelAdmin):
    pass
