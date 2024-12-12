from django.urls import path, include
from .views import CreateExamCard, ExamListView, ListCreateQuestions, ExamDetailView, CreateResultView

urlpatterns = [
    path('exam', ExamListView.as_view()),
    path('exam/create', CreateExamCard.as_view()),
    path('exam/<uuid:uuid>', ExamDetailView.as_view(), name='exam-detail'),  # URL с UUID
    path('question', ListCreateQuestions.as_view()),
    path('result', CreateResultView.as_view()),

]