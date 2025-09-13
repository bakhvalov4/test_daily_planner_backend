from django.contrib import admin
from .models import Daily


@admin.register(Daily)
class DailyAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_done', 'created_at')
    list_editable = ('is_done',)
    search_fields = ('title',)
