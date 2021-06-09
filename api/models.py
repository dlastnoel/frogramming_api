from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return str(self.id) + ' ' + self.username


class Module(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    module = models.FileField(max_length=255)

    def __str__(self):
        return str(self.id) + ' ' + self.name


class Quiz(models.Model):
    name = models.CharField(max_length=255)
    module_id = models.ForeignKey(Module, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.module_id.name + ' - ' + '(' + str(self.id) + ') ' + self.name


class Question(models.Model):

    TYPE_CHOICES = (
        ('fill', 'Fill in the blanks'),
        ('choice', 'Multiple choice'),
        ('tf', 'True or False'),
    )
    quiz_id = models.ForeignKey(Quiz, null=True, on_delete=models.SET_NULL)
    type = models.CharField(max_length=255, choices=TYPE_CHOICES)
    question = models.TextField()
    choice = models.TextField(null=True, blank=True)
    correct_answer = models.CharField(max_length=255)

    def __str__(self):
        return self.quiz_id.name + ' - ' + str(self.id) + ' ' + self.question


class Answer(models.Model):
    user_id = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    quiz_id = models.ForeignKey(Quiz, null=True, on_delete=models.SET_NULL)
    question_id = models.ForeignKey(
        Question, null=True, on_delete=models.SET_NULL)
    user_answer = models.CharField(max_length=255)

    def __str__(self):
        return '(User ' + self.user_id.username + ') (' + str(self.question_id) + ') ' + ' - ' + str(self.user_answer)


class UserQuiz(models.Model):
    user_id = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    quiz_id = models.ForeignKey(Quiz, null=True, on_delete=models.SET_NULL)
    total = models.IntegerField(null=True, blank=True)
    score = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return '(User: ' + self.user_id.username + ') - ' + str(self.quiz_id)
