# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('school_tag', models.CharField(help_text=b'School', max_length=20, choices=[(b'business', b'Adam Smith Business School'), (b'cardiovascular', b'Institute of Cardiovascular and Med Sci'), (b'architecture', b'Mackintosh School of Architecture'), (b'chemistry', b'School of Chemistry'), (b'computing', b'School of Computing Science'), (b'critical', b'School of Critical Studies'), (b'culture', b'School of Culture and Creative Arts'), (b'education', b'School of Education'), (b'engineering', b'School of Engineering'), (b'geography', b'School of Geography and Earth Sciences'), (b'humanities', b'School of Humanities'), (b'interdisciplinary', b'School of Interdisciplinary Studies'), (b'law', b'School of Law'), (b'life', b'School of Life Sciences'), (b'maths', b'School of Mathematics and Statistics'), (b'medicine', b'School of Medicine'), (b'mlc', b'School of MLC'), (b'physics', b'School of Physics and Astronomy'), (b'psychology', b'School of Psychology'), (b'social', b'School of Social and Political Sciences'), (b'veterinary', b'School of Veterinary Medicine')])),
                ('title', models.CharField(max_length=128)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.CharField(max_length=256)),
                ('lecturer', models.CharField(max_length=128)),
                ('total_rating', models.IntegerField(default=0)),
                ('quantity_ratings', models.IntegerField(default=0)),
                ('average_rating', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.IntegerField(blank=True, help_text=b'Rate this course between 1 and 5', null=True, choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('text', models.CharField(max_length=256, blank=True)),
                ('course', models.ForeignKey(to='good_course.Course')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('tag', models.CharField(unique=True, max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lecturer', models.BooleanField(default=False, help_text=b'Lecturer?')),
                ('picture', models.ImageField(help_text=b'Picture?', upload_to=b'profile_images', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='course',
            name='school',
            field=models.ForeignKey(to='good_course.School'),
            preserve_default=True,
        ),
    ]
