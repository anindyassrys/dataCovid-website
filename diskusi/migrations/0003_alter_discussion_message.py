# Generated by Django 3.2.7 on 2021-10-30 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diskusi', '0002_discussion_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussion',
            name='message',
            field=models.CharField(max_length=2500),
        ),
    ]
