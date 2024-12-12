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



class ExamListView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            # Получаем экзамены для текущего пользователя
            exams = ExamCard.objects.filter(user=request.user)
            if exams:# Фильтруем по текущему пользователю
                serializer = ExamCardSerializer(exams, many=True)
                return Response(serializer.data)
            else:
                return Response({'detail': "пусто"})
        else:
            return Response(
                {"detail": "Authentication credentials were not provided."},
                status=status.HTTP_401_UNAUTHORIZED
            )

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