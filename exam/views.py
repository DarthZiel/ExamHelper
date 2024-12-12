from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ExamCardSerializer
from .models import ExamCard
# Create your views here.

class CreateExamCard(generics.CreateAPIView):
    serializer_class = ExamCardSerializer
    queryset = ExamCard.objects.all()



class ExamListView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            # Получаем экзамены для текущего пользователя
            exams = ExamCard.objects.filter(user=request.user)  # Фильтруем по текущему пользователю
            serializer = ExamCardSerializer(exams, many=True)
            return Response(serializer.data)
        else:
            return Response(
                {"detail": "Authentication credentials were not provided."},
                status=status.HTTP_401_UNAUTHORIZED
            )