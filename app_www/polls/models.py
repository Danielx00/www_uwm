from django.db import models
import datetime
from django.utils import timezone
from datetime import date
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

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


class Druzyna(models.Model):
    nazwa = models.TextField(max_length=33)
    kraj = models.TextField(max_length=2)

    def __str__(self):
        return '%s (%s)' % (self.nazwa, self.kraj)


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

class Osoba(models.Model):

    class Meta:
        ordering = ('nazwisko',)

    imie = models.TextField(blank=False, max_length=33)
    nazwisko = models.TextField(blank=False, max_length=40)
    miesiac_urodzenia = models.IntegerField(choices=MONTHS.choices, default=timezone.now().month)
    data_dodania = models.DateField(auto_now_add=True)
    wlasciciel = models.ForeignKey('auth.User', null=True, on_delete=models.CASCADE)
    can_view_other_persons = models.BooleanField(default=False)
    druzyna = models.ForeignKey(
        Druzyna,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.imie + ' ' + self.nazwisko

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)




