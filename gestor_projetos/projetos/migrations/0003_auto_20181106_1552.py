# Generated by Django 2.0.5 on 2018-11-06 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0002_assignment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignment',
            old_name='prject_id',
            new_name='project_id',
        ),
    ]
