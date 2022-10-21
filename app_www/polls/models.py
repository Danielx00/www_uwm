from django.db import models
import datetime
from django.utils import timezone

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
    DATA_OPTIONS = (
        ('1', 'Styczen'),
        ('2', 'Luty'),
        ('3', 'Marzec'),
        ('4', 'Kwiecien'),
        ('5', 'Maj'),
        ('6', 'Czerwiec'),
        ('7', 'Lipiec'),
        ('8', 'Sierpien'),
        ('9', 'Wrzesien'),
        ('10', 'Pazdziernik'),
        ('11', 'Listopad'),
        ('12', 'Grudzien'),
    )
    imie = models.TextField(blank=False, max_length=33)
    naziwsko = models.TextField(blank=False, max_length=40)
    miesiac_urodzenia = models.CharField(max_length=2, choices=DATA_OPTIONS, default='Styczen')
