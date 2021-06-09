from api.models import *
from django.contrib import admin


# Header
admin.site.site_header = 'Frogramming'
admin.site.site_title = 'Frogramming'
admin.site.index_title = 'Frogramming'
#  Register your models here.
admin.site.register(User)
admin.site.register(Module)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(UserQuiz)
