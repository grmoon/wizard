# Generated by Django 2.2 on 2019-04-07 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wizard', '0005_auto_20190407_2100'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='trigger',
            unique_together={('position', 'from_question', 'to_question'), ('to_question', 'from_question', 'value', 'condition')},
        ),
    ]
