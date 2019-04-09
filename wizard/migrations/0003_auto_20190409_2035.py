# Generated by Django 2.2 on 2019-04-09 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wizard', '0002_field_default'),
    ]

    operations = [
        migrations.CreateModel(
            name='SelectField',
            fields=[
                ('multiplechoicefield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wizard.MultipleChoiceField')),
                ('autocomplete', models.BooleanField(default=False)),
                ('autofocus', models.BooleanField(default=False)),
                ('disabled', models.BooleanField(default=False)),
                ('multiple', models.BooleanField(default=False)),
                ('required', models.BooleanField(default=False)),
                ('size', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wizard.multiplechoicefield',),
        ),
        migrations.CreateModel(
            name='SelectOption',
            fields=[
                ('multiplechoiceoption_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wizard.MultipleChoiceOption')),
                ('position', models.PositiveIntegerField()),
                ('disabled', models.BooleanField(default=False)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wizard.SelectField')),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wizard.Option')),
            ],
            options={
                'abstract': False,
                'unique_together': {('position', 'field', 'option')},
            },
            bases=('wizard.multiplechoiceoption',),
        ),
        migrations.AddField(
            model_name='selectfield',
            name='options',
            field=models.ManyToManyField(through='wizard.SelectOption', to='wizard.Option'),
        ),
    ]