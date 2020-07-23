# Generated by Django 2.1.15 on 2020-07-23 09:43

from django.db import migrations


def set_custom_action_code(apps, schema_editor):
    CustomActionExecution = apps.get_model('rdrf', 'CustomActionExecution')
    for cae in CustomActionExecution.objects.all():
        cae.custom_action_code = cae.custom_action.code
        cae.save()


class Migration(migrations.Migration):

    dependencies = [
        ('rdrf', '0132_customactionexecution_custom_action_code'),
    ]

    operations = [
        migrations.RunPython(set_custom_action_code),
    ]
