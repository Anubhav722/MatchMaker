from django.contrib import admin
from .models import *

# Register your models here.

class AnswerTabularInline(admin.TabularInline):
	model = Answer

class QuestionAdmin(admin.ModelAdmin):
	inlines = [AnswerTabularInline]
	class Meta:
		model = Question

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(UserAnswer)