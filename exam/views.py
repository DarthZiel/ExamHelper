from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from .serializers import ExamCardSerializer
from .models import ExamCard
# Create your views here.

class CreateExamCard(generics.CreateAPIView):
    serializer_class = ExamCardSerializer
    queryset = ExamCard.objects.all()