# Generated by Django 3.2.4 on 2021-10-15 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0004_emp1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='files')),
            ],
        ),
    ]