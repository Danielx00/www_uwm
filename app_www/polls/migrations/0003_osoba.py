# Generated by Django 4.1.2 on 2022-10-21 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_alter_choice_choice_text_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Osoba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.TextField(max_length=33)),
                ('naziwsko', models.TextField(max_length=40)),
                ('miesiac_urodzenia', models.CharField(choices=[('1', 'Styczen'), ('2', 'Luty'), ('3', 'Marzec'), ('4', 'Kwiecien'), ('5', 'Maj'), ('6', 'Czerwiec'), ('7', 'Lipiec'), ('8', 'Sierpien'), ('9', 'Wrzesien'), ('10', 'Pazdziernik'), ('11', 'Listopad'), ('12', 'Grudzien')], max_length=2)),
            ],
        ),
    ]
