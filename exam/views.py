from django.core.serializers import serialize
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ExamCardSerializer, QuestionSerializer, ExamCardDetailSerializer
from .models import ExamCard, Question


# Create your views here.

class CreateExamCard(generics.CreateAPIView):
    serializer_class = ExamCardSerializer
    queryset = ExamCard.objects.all()



class ExamListView(generics.ListAPIView):
    queryset = ExamCard.objects.all()
    serializer_class = ExamCardSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Получаем записи только для текущего авторизованного пользователя
        return ExamCard.objects.filter(user=self.request.user)

class ListCreateQuestions(generics.ListCreateAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class ExamDetailView(generics.RetrieveAPIView):
    serializer_class = ExamCardDetailSerializer
    queryset = ExamCard.objects.all()
    # def get_queryset(self):
    #     # Возвращаем только экзамены текущего пользователя
    #     return ExamCard.objects.filter(user=self.request.user)

    lookup_field = 'uuid'  # Поиск по UUID