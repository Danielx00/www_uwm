from django.contrib import admin

# Register your models here.
from .models import Question
from .models import Osoba
from .models import Druzyna


class OsobaAdmin(admin.ModelAdmin):
    list_display = ['imie', 'nazwisko', 'miesiac_urodzenia', 'data_dodania']

class DruzynaAdmin(admin.ModelAdmin):
    list_display = ['nazwa', 'kraj']

admin.site.register(Question)
admin.site.register(Osoba, OsobaAdmin)
admin.site.register(Druzyna)