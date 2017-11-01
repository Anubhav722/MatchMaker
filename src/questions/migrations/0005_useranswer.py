# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0004_auto_20171029_1649'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('my_answer_importance', models.CharField(choices=[('Mandatory', 'Mandatory'), ('Very Important', 'Very Important'), ('Somewhat Important', 'Somewhat Important'), ('Not Important', 'Not Important')], max_length=50)),
                ('their_answer_importance', models.CharField(choices=[('Mandatory', 'Mandatory'), ('Very Important', 'Very Important'), ('Somewhat Important', 'Somewhat Important'), ('Not Important', 'Not Important')], max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('my_answer', models.ForeignKey(related_name='user_answer', to='questions.Answer')),
                ('question', models.ForeignKey(to='questions.Question')),
                ('their_answer', models.ForeignKey(related_name='match_answer', null=True, blank=True, to='questions.Answer')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
