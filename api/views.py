from django.db.models.base import Model
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import response

from rest_framework.decorators import api_view
from rest_framework.response import Response

from random import sample

from .models import *
from .serializers import *

# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Users': '/users/<str:pk>',
        'Modules': '/modules/<str:pk>',
        'Quizzes': '/quizzes/<str:pk>/',
        'Questions': '/questions/<str:pk>',
        'Choices': '/choices/<str:pk>/',
        'Answers add': '/answers/<str:pk>',
        'Users add': '/users/add/',
        'Modules add': '/module/add/',
        'Quizzes add': '/quiz/add//',
        'Questions add': '/question/add/',
        'Answers add': '/answer/add/',
    }
    return Response(api_urls)


@api_view(['GET'])
def Users(request, pk):
    if(pk == 'all'):
        users = User.objects.all()
    else:
        users = User.objects.filter(id=pk)

    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def Modules(request, pk):
    if(pk == 'all'):
        modules = Module.objects.all()
    else:
        modules = Module.objects.get(id=pk)

    serializer = ModuleSerializer(modules, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def Quizzes(request, pk):
    if(pk == 'all'):
        quizzes = Quiz.objects.all()
    else:
        quizzes = Quiz.objects.filter(module_id=pk)

    serializer = QuizSerializer(quizzes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def Questions(request, pk):
    if(pk == 'all'):
        count = Question.objects.all().count()
        questions = Question.objects.all().order_by('?')[:count]
    else:
        questions = Question.objects.filter(quiz_id=pk)

    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def Answers(request, pk):
    if(pk == 'all'):
        answers = Answer.objects.all()
    else:
        answers = Answer.objects.get(id=pk)

    serializer = AnswerSerializer(answers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def UserQuizzes(request, pk):
    if(pk == 'all'):
        userquizzes = UserQuiz.objects.all()
    else:
        userquizzes = UserQuiz.objects.get(id=pk)

    serializer = UserQuizSerializer(userquizzes, many=True)
    return Response(serializer.data)


@ api_view(['POST'])
def UserAdd(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@ api_view(['POST'])
def ModuleAdd(request):
    serializer = ModuleSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@ api_view(['POST'])
def QuizAdd(request):
    serializer = QuizSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@ api_view(['POST'])
def QuestionAdd(request):
    serializer = QuestionAdd(data=request.data)

    if serializer.is_valid():
        serializer.save()
    else:
        print('error')

    return Response(serializer.data)


@ api_view(['POST'])
def AnswerAdd(request):
    serializer = AnswerSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@ api_view(['POST'])
def UserQuizAdd(request):
    serializer = UserQuizSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@ api_view(['POST'])
def CheckUserQuiz(request):
    serializer = UserQuizSerializer(data=request.data)
    if serializer.is_valid():
        request_user_id = request.data['user_id']
        request_quiz_id = request.data['quiz_id']
        user_quiz = UserQuiz.objects.filter(
            user_id=request_user_id, quiz_id=request_quiz_id).exists()
        response = {
            'response': user_quiz
        }

    return Response(response)


@ api_view(['POST'])
def ViewUserScore(request):
    serializer = UserQuizSerializer(data=request.data)
    if serializer.is_valid():
        request_user_id = request.data['user_id']
        request_quiz_id = request.data['quiz_id']
        user_quiz = UserQuiz.objects.get(
            user_id=request_user_id, quiz_id=request_quiz_id)
        results = {
            'user_id': request_user_id,
            'quiz_id': request_quiz_id,
            'total': user_quiz.total,
            'score': user_quiz.score
        }
    return Response(results)
