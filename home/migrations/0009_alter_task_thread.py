# Generated by Django 3.2.7 on 2021-10-18 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_rename_tasktitle_threads_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='thread',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.threads'),
        ),
    ]