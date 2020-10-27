# Generated by Django 2.2.12 on 2020-08-24 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobsPortal', '0007_auto_20200824_1937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lamaran',
            name='judul_job',
        ),
        migrations.RemoveField(
            model_name='lamaran',
            name='slug_job',
        ),
        migrations.AddField(
            model_name='lamaran',
            name='judul',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='jobsPortal.Job'),
            preserve_default=False,
        ),
    ]
