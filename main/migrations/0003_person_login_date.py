# Generated by Django 4.0.1 on 2022-01-16 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_person_id_alter_person_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='login_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
