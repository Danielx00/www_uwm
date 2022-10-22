from django.contrib import admin

# Register your models here.
from .models import Question
from .models import Osoba


class OsobaAdmin(admin.ModelAdmin):
    list_display = ['imie', 'nazwisko', 'miesiac_urodzenia', 'data_dodania']

admin.site.register(Question)
admin.site.register(Osoba, OsobaAdmin)