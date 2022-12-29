# Generated by Django 4.1.3 on 2022-12-29 13:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_subscribers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='subscribers',
        ),
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Автор', to=settings.AUTH_USER_MODEL)),
                ('follower', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Подписчик', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
