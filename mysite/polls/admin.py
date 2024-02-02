from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Choice, Question

from .models import Question

admin.site.register(Question)




class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]
    list_display = ["question_text", "pub_date"]
    list_display = ["question_text", "pub_date", "was_published_recently"]

admin.site.register(Question, QuestionAdmin)


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]


admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)


class ChoiceInline(admin.TabularInline):