from django.db.models.base import Model
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import *

# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List of Officials': '/officials/',
        'Official Details': '/officials/<str:pk>/',
        'Cases': '/cases/',
        'Case Count': '/cases/count/',
        'Posts': '/posts/<str:type>',
        'Request Details': '/requests/<str:pk>',
        'Request Create': '/request-create/',
        'Request Update': '/request-update/',
    }
    return Response(api_urls)


@api_view(['GET'])
def Users(request, pk):
    if(pk == 'all'):
        users = User.objects.all()
    else:
        users = User.objects.get(id=pk)

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
        quizzes = Quiz.objects.get(id=pk)

    serializer = QuizSerializer(quizzes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def Questions(request, pk):
    if(pk == 'all'):
        questions = Question.objects.all()
    else:
        questions = Question.objects.get(id=pk)

    serializer = ModuleSerializer(questions, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def Choices(request, pk):
    if(pk == 'all'):
        choices = Choice.objects.all()
    else:
        choices = Choice.objects.get(id=pk)

    serializer = ModuleSerializer(choices, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Answers(request, pk):
    if(pk == 'all'):
        answers = Answers.objects.all()
    else:
        answers = Answers.objects.get(id=pk)

    serializer = ModuleSerializer(answers, many=True)
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

    return Response(serializer.data)


@ api_view(['POST'])
def ChoiceAdd(request):
    serializer = QuestionSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@ api_view(['POST'])
def AnswerAdd(request):
    serializer = AnswerSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
