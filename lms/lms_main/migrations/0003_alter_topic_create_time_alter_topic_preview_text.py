# Generated by Django 4.1.3 on 2022-12-22 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_main', '0002_category_rename_date_topic_create_time_topic_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='preview_text',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]