from django.contrib.auth import get_user_model
from rest_framework import serializers
from . import models

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Question
        fields = ["url", "id", "text", "answer_set"]

class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Answer
        fields = ["url", "id", "text", "question", "vote_set"]

class VoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Vote
        fields = ["url", "id", "answer", "user"]

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["url", "id", "username", "email", "vote_set"]