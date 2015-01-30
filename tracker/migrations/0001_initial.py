# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionRecord',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('date', models.DateTimeField()),
                ('action', models.TextField()),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Allotment',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('hours', models.DecimalField(decimal_places=3, max_digits=10)),
                ('expiry', models.DateField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AllotmentType',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=30)),
                ('default_hours', models.DecimalField(decimal_places=3, null=True, blank=True, max_digits=10)),
                ('max_hours', models.DecimalField(decimal_places=3, null=True, blank=True, max_digits=10)),
                ('default_expiry_period', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AllotmentTypeOverride',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('default_hours', models.DecimalField(decimal_places=3, null=True, blank=True, max_digits=10)),
                ('max_hours', models.DecimalField(decimal_places=3, null=True, blank=True, max_digits=10)),
                ('default_expiry_period', models.IntegerField()),
                ('type', models.ForeignKey(to='tracker.AllotmentType')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('hours', models.DecimalField(decimal_places=3, max_digits=10)),
                ('notes', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RequestState',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=30)),
                ('forward_state', models.ForeignKey(related_name='request_forward_state', to='tracker.RequestState')),
                ('reverse_state', models.ForeignKey(related_name='request_reverse_state', to='tracker.RequestState')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='request',
            name='state',
            field=models.ForeignKey(to='tracker.RequestState'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='request',
            name='type',
            field=models.ForeignKey(to='tracker.AllotmentType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='request',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='allotment',
            name='type',
            field=models.ForeignKey(to='tracker.AllotmentType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='allotment',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
