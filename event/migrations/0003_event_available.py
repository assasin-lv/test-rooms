# Generated by Django 4.1 on 2022-08-18 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_alter_event_type_event_reservation'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
