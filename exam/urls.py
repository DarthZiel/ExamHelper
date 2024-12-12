from django.urls import path, include
from .views import CreateExamCard


urlpatterns = [

    path('exam/', CreateExamCard.as_view()),
]