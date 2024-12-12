
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from .utils import evalute

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


    def perform_create(self, serializer):
        # try:
        #     q_and_a = self.request.data.get('q_and_a')
        #     res = evalute(q_and_a)
        #     result_instance = serializer.save(mark=res)
        # except:
        #     result_instance = serializer.save(mark='50%')
        #
        result_instance = serializer.save(mark='50%')
        return result_instance
