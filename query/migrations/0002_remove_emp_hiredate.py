# Generated by Django 3.2.4 on 2021-10-03 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emp',
            name='hiredate',
        ),
    ]
