from django.contrib import admin
from .models import Question, ExamCard, Result
# Register your models here.


admin.site.register(Question)

admin.site.register(Result)

class ExamCardAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'title')  # Укажите нужные поля для отображения
                  # Добавляет фильтр по дате

admin.site.register(ExamCard, ExamCardAdmin)