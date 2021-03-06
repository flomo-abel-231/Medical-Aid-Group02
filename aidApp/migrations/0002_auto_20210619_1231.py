# Generated by Django 3.2.4 on 2021-06-19 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aidApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consultations',
            old_name='patient_full_name',
            new_name='patient_last_name',
        ),
        migrations.RenameField(
            model_name='feedback_complaint',
            old_name='patient_full_name',
            new_name='patient_first_name',
        ),
        migrations.RenameField(
            model_name='patients',
            old_name='patient_full_name',
            new_name='patient_first_name',
        ),
        migrations.AddField(
            model_name='patients',
            name='patient_last_name',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
