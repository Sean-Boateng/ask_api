# Generated by Django 5.0.2 on 2024-02-22 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('response', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='response',
            old_name='prompt',
            new_name='prompt_id',
        ),
    ]