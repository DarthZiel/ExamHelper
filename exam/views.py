
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ExamCardSerializer, QuestionSerializer, ExamCardDetailSerializer, GetResultSerializer
from .models import ExamCard, Question, Result


# Create your views here.

class CreateExamCard(generics.CreateAPIView):
    serializer_class = ExamCardSerializer
    queryset = ExamCard.objects.all()

    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ExamListView(generics.ListAPIView):
    queryset = ExamCard.objects.all()
    serializer_class = ExamCardDetailSerializer
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




class CreateResultView(generics.CreateAPIView):
    serializer_class = GetResultSerializer
    queryset = Result.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        q_and_a = self.request.data.get('q_and_a')
        # external_api_url = 'https://external-api.com/data'  # Укажите URL внешнего API
        # response = requests.get(external_api_url, params={'title': title, 'date': date})
        #
        # if response.status_code == 200:
        #     external_data = response.json()  # Получаем ответ от внешнего API
        #
        #     # Дополняем данные для создания записи
        #     # Пример: добавляем данные из внешнего API
        #     extra_field = external_data.get('extra_field', None)
        #
        #     # Сохраняем объект с дополнительными данными
        #     serializer.save(user=self.request.user, extra_field=extra_field)
        # else:
        #     # Обработка ошибок, если внешний API вернул ошибку
        #     raise Exception("Error fetching data from external API")
