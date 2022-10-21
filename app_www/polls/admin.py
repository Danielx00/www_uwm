from django.contrib import admin

# Register your models here.
from .models import Question
from .models import Osoba

admin.site.register(Question)
admin.site.register(Osoba)