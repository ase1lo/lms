# Generated by Django 4.1.3 on 2022-12-14 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=30, null=True, verbose_name='Ник'),
        ),
    ]
