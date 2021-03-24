from django.contrib import admin

from .models import Answer

# Register your models here.
@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['owner', 'score']
    list_filter = ['creation_date', 'last_edit_date']
    search_fields = ['body']