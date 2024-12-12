from rest_framework.serializers import ModelSerializer, CharField
from .models import ExamCard, Result, Question, User

class ExamCardSerializer(ModelSerializer):
    user = CharField(source='user.username')  # Берем username пользователя

    class Meta:
        model = ExamCard
        fields = '__all__'


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']




class ExamCardSerializer(ModelSerializer):

    # user = UserSerializer()
    class Meta:
        model = ExamCard
        fields = ['uuid','title']


class QuestionSerializer(ModelSerializer):

    class Meta:
        model = Question
        fields = '__all__'

class ResultSerializer(ModelSerializer):
    class Meta:
        model = Result
        fields = ['fio', 'mark']


class ExamCardDetailSerializer(ModelSerializer):
    questions = QuestionSerializer(many=True)  # Вложенный сериализатор
    results = ResultSerializer(many=True)
    class Meta:
        model = ExamCard
        fields = ['uuid', 'title', 'questions']  # Укажите необходимые поля


class GetResultSerializer(ModelSerializer):
    class Meta:
        model = Result
        fields = ['fio', 'q_and_a', 'exam_card']
