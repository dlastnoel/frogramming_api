from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('users/<str:pk>/', views.Users, name='users'),
    path('modules/<str:pk>/', views.Modules, name='modules'),
    path('quizzes/<str:pk>/', views.Quizzes, name='quizzes'),
    path('questions/<str:pk>/', views.Questions, name='questions'),
    path('answers/<str:pk>/', views.Answers, name='answers'),
    path('userquizzes/<str:pk>/', views.UserQuizzes, name='userquizzes'),

    path('user/add/', views.UserAdd, name='user-add'),
    path('module/add/', views.ModuleAdd, name='modules-add'),
    path('quiz/add/', views.QuizAdd, name='quiz-add'),
    path('question/add/', views.QuestionAdd, name='questions-add'),
    path('answer/add/', views.AnswerAdd, name='answers-add'),
    path('userquiz/add/', views.UserQuizAdd, name='userquiz-add'),
    path('checkuserquiz/', views.CheckUserQuiz, name='checkuserquiz'),
]
