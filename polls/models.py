from django.db import models
from django.conf import settings
from django.urls import reverse

class Question(models.Model):
    text = models.CharField(max_length=256)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('question', args=[self.id])


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=256)

    def __str__(self):
        return self.text


class Vote(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.answer.text}/{self.user.name}"
