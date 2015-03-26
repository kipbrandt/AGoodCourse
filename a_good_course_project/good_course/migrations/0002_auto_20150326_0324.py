# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('good_course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.IntegerField(help_text=b'Rate this course between 1 and 5', validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='lecturer',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.CharField(help_text=b'Description: (max 256 characters)', max_length=256),
        ),
        migrations.AlterField(
            model_name='course',
            name='lecturer',
            field=models.CharField(help_text=b'Lecturer:', max_length=128),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(help_text=b'Course title:', max_length=128),
        ),
    ]
