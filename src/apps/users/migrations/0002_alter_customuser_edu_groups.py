# Generated by Django 4.0.5 on 2022-06-12 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='edu_groups',
            field=models.ManyToManyField(blank=True, null=True, related_name='students', to='users.group'),
        ),
    ]