# Generated by Django 4.1 on 2022-08-18 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('capacity', models.IntegerField(default=12)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type_event', models.CharField(choices=[(1, 'Public'), (2, 'Privado')], max_length=1)),
                ('room', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='event.room')),
            ],
        ),
    ]
