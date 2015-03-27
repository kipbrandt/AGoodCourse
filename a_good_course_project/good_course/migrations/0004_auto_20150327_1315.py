# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('good_course', '0003_auto_20150327_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(default=0, help_text=b'Rate this course between 1 and 5', choices=[(0, b''), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
        ),
    ]
