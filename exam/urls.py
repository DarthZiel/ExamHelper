from django.urls import path, include
from .views import CreateExamCard, ExamListView


urlpatterns = [
    path('exam/', ExamListView.as_view()),
    path('exam/create', CreateExamCard.as_view()),

]