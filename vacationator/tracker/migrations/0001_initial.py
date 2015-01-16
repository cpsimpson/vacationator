# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allotment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('type', models.CharField(max_length=30, choices=[('vacation', 'Vacation')])),
                ('hours', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
