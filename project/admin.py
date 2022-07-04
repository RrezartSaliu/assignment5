from django.contrib import admin

from project.models import Account, Question


class AccountAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']


admin.site.register(Account, AccountAdmin)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'question']


admin.site.register(Question, QuestionAdmin)
