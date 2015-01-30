# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requeststate',
            name='forward_state',
            field=models.ForeignKey(related_name='request_forward_state', blank=True, null=True, to='tracker.RequestState'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='requeststate',
            name='reverse_state',
            field=models.ForeignKey(related_name='request_reverse_state', blank=True, null=True, to='tracker.RequestState'),
            preserve_default=True,
        ),
    ]
