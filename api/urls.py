from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('users/<str:pk>/', views.Users, name='users'),
    path('modules/<str:pk>/', views.Modules, name='modules'),
    path('quizzes/<str:pk>/', views.Quizzes, name='quizzes'),
    path('questions/<str:pk>/', views.Questions, name='questions'),
    path('choices/<str:pk>/', views.Choices, name='choices'),
    path('answers/<str:pk>/', views.Answers, name='answers'),

    path('modules/add/', views.ModuleAdd, name='modules-add'),
    path('quizzes/add/', views.QuizAdd, name='quizzes-add'),
    path('questions/add/', views.QuestionAdd, name='questions-add'),
    path('choices/add.', views.ChoiceAdd, name='choices-add'),
    path('answers/add/', views.AnswerAdd, name='answers-add'),
]
