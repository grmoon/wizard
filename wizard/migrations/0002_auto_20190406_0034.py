# Generated by Django 2.2 on 2019-04-06 00:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wizard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trigger',
            name='position',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='question',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='trigger',
            unique_together={('option', 'position')},
        ),
        migrations.CreateModel(
            name='SectionQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveIntegerField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wizard.Question')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wizard.Section')),
            ],
            options={
                'unique_together': {('position', 'question', 'section')},
            },
        ),
        migrations.RemoveField(
            model_name='question',
            name='position',
        ),
        migrations.RemoveField(
            model_name='question',
            name='section',
        ),
        migrations.AddField(
            model_name='section',
            name='questions',
            field=models.ManyToManyField(through='wizard.SectionQuestion', to='wizard.Question'),
        ),
    ]
