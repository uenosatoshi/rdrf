# Generated by Django 2.1.15 on 2020-06-10 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rdrf', '0123_auto_20200504_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveyquestion',
            name='widget_config',
            field=models.TextField(blank=True, null=True),
        ),
    ]
