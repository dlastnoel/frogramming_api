from django.db.models import fields
from rest_framework import serializers
from rest_framework.fields import Field
from .models import *
from django.conf import settings


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ModuleSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField('get_url')

    def get_url(self, obj):
        return '%s%s' % (settings.MEDIA_URL, obj.module)

    class Meta:
        model = Module
        fields = ('id', 'name', 'url')


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class UserQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserQuiz
        fields = '__all__'


class LeaderboardsSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user_id.username')

    class Meta:
        model = UserQuiz
        fields = ('id', 'total', 'score',
                  'user_id', 'quiz_id', 'username')
