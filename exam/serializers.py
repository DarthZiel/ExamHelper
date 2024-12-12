from rest_framework.serializers import ModelSerializer
from .models import ExamCard, Result, Question, User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']




class ExamCardSerializer(ModelSerializer):

    # user = UserSerializer()
    class Meta:
        model = ExamCard
        fields = '__all__'