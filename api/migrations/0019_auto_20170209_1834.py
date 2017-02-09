# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-09 23:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_hackathonsponsor_on_mobile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendeestatus',
            old_name='rsvp_confirmed',
            new_name='rsvp_result',
        ),
        migrations.RemoveField(
            model_name='attendeestatus',
            name='checked_in',
        ),
        migrations.RemoveField(
            model_name='attendeestatus',
            name='checked_in_timestamp',
        ),
        migrations.RemoveField(
            model_name='attendeestatus',
            name='rsvp_confirmed_timestamp',
        ),
        migrations.RemoveField(
            model_name='attendeestatus',
            name='rsvp_email_sent',
        ),
        migrations.RemoveField(
            model_name='attendeestatus',
            name='rsvp_email_sent_timestamp',
        ),
        migrations.AddField(
            model_name='attendeestatus',
            name='checked_in_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='attendeestatus',
            name='extra_info',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AddField(
            model_name='attendeestatus',
            name='rsvp_email_sent_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='attendeestatus',
            name='rsvp_submitted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='attendeestatus',
            name='comments',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
    ]
