from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import *

admin.site.register(get_user_model())

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("text", "question", "vote_count")
    list_filter = ("question", )
    search_fields = ("text", )

    def vote_count(self, obj):
        return obj.vote_set.count()

    vote_count.short_description = "Votes"

class AnswerInline(admin.StackedInline):
    model = Answer

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]


