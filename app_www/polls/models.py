from django.db import models
import datetime
from django.utils import timezone
from datetime import date

class Question(models.Model):
    question_text = models.CharField(max_length=150)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=150)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Osoba(models.Model):

    class Meta:
        ordering = ('nazwisko',)

    class MONTHS(models.IntegerChoices):
        STYCZEN = 1
        LUTY = 2
        MARZEC = 3
        KWIECIEN = 4
        MAJ = 5
        CZERWIEC = 6
        LIPIEC = 7
        SIERPIEN = 8
        WRZESIEN = 9
        PAZDZIERNIK = 10
        LISTOPAD = 11
        GRUDZIEN = 12

    imie = models.TextField(blank=False, max_length=33)
    nazwisko = models.TextField(blank=False, max_length=40)
    miesiac_urodzenia = models.IntegerField(choices=MONTHS.choices, default=MONTHS.STYCZEN)
    data_dodania = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.imie + ' ' + self.nazwisko


