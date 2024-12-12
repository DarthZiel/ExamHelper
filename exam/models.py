import uuid
from django.db import models
from django.contrib.auth import get_user_model



User = get_user_model()

class ExamCard(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='examcard')

    def __str__(self):
        return self.title


class Question(models.Model):
    exam_card = models.ForeignKey(
        ExamCard, on_delete=models.CASCADE, related_name="questions"
    )
    text = models.TextField()  # Текст вопроса


    def __str__(self):
        return f"Question in {self.exam_card.title}"

class Result(models.Model):
    fio = models.CharField(max_length=100)
    mark = models.CharField(max_length=10, blank=True)
    q_and_a = models.TextField()
    exam_card = models.ForeignKey(
        ExamCard, on_delete=models.CASCADE, related_name="results")
