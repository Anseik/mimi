# Generated by Django 3.1.7 on 2021-03-16 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='id',
            field=models.EmailField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='member',
            name='password',
            field=models.CharField(max_length=200),
        ),
    ]
