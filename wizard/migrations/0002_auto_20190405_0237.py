# Generated by Django 2.2 on 2019-04-05 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wizard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radiobuttonoption',
            name='field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='wizard.RadioButtonField'),
        ),
    ]
