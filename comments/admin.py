from django.contrib import admin

from .models import CommentOnQuestion, CommentOnAnswer

# Register your models here.
@admin.register(CommentOnQuestion)
class CommentOnQuestionAdmin(admin.ModelAdmin):
    list_display = ['owner', 'active']


@admin.register(CommentOnAnswer)
class CommentOnAnswerAdmin(admin.ModelAdmin):
    list_display = ['owner', 'active']