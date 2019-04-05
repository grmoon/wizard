# Generated by Django 2.2 on 2019-04-05 22:46

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('content_type', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_type', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveIntegerField()),
                ('text', models.CharField(max_length=256)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wizard.Field')),
            ],
        ),
        migrations.CreateModel(
            name='Wizard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MultipleChoiceField',
            fields=[
                ('field_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wizard.Field')),
            ],
            options={
                'abstract': False,
            },
            bases=('wizard.field',),
        ),
        migrations.CreateModel(
            name='Trigger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='triggers', to='wizard.Option')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='triggered_by', to='wizard.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveIntegerField()),
                ('wizard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='wizard.Wizard')),
            ],
            options={
                'unique_together': {('position', 'wizard')},
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('position', models.PositiveIntegerField()),
                ('step', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='wizard.Step')),
            ],
            options={
                'unique_together': {('name', 'step'), ('position', 'step')},
            },
        ),
        migrations.AddField(
            model_name='question',
            name='section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='wizard.Section'),
        ),
        migrations.CreateModel(
            name='RadioButtonField',
            fields=[
                ('multiplechoicefield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wizard.MultipleChoiceField')),
                ('required', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('wizard.multiplechoicefield',),
        ),
        migrations.AlterUniqueTogether(
            name='question',
            unique_together={('section', 'position')},
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', django.contrib.postgres.fields.jsonb.JSONField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='wizard.Question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('question', 'user')},
            },
        ),
        migrations.CreateModel(
            name='RadioButtonOption',
            fields=[
                ('option_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wizard.Option')),
                ('label', models.CharField(max_length=256)),
                ('position', models.PositiveIntegerField()),
                ('value', models.CharField(max_length=256)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='wizard.RadioButtonField')),
            ],
            options={
                'abstract': False,
                'unique_together': {('field', 'value'), ('field', 'position'), ('field', 'label')},
            },
            bases=('wizard.option', models.Model),
        ),
    ]
