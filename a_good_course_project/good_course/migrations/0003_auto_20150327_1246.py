# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('good_course', '0002_auto_20150327_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='average_rating',
            field=models.DecimalField(max_digits=2, decimal_places=1),
        ),
    ]
