# Generated by Django 2.0.5 on 2018-11-07 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0003_auto_20181106_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='description',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]
