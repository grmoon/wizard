# Generated by Django 2.2 on 2019-04-11 22:28

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=256, unique=True)),
                ('content_type', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FileAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('label', models.CharField(max_length=256)),
                ('value', models.CharField(max_length=256)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('text', models.CharField(max_length=256)),
                ('content_type', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=256)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=256, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Wizard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=256, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FileField',
            fields=[
                ('field_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wizard.Field')),
                ('accept', models.CharField(blank=True, max_length=256, null=True)),
                ('multiple', models.BooleanField(default=False)),
                ('required', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('wizard.field',),
        ),
        migrations.CreateModel(
            name='JSONField',
            fields=[
                ('field_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wizard.Field')),
            ],
            options={
                'abstract': False,
            },
            bases=('wizard.field',),
        ),
        migrations.CreateModel(
            name='JSONQuestion',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wizard.Question')),
                ('default', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wizard.JSONField')),
            ],
            options={
                'abstract': False,
            },
            bases=('wizard.question',),
        ),
        migrations.CreateModel(
            name='WizardStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('position', models.PositiveIntegerField()),
                ('step', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wizard.Step')),
                ('wizard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wizard.Wizard')),
            ],
            options={
                'unique_together': {('position', 'wizard'), ('wizard', 'step')},
            },
        ),
        migrations.AddField(
            model_name='wizard',
            name='steps',
            field=models.ManyToManyField(through='wizard.WizardStep', to='wizard.Step'),
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='value', to='wizard.FileAnswer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StepSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('position', models.PositiveIntegerField()),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wizard.Section')),
                ('step', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wizard.Step')),
            ],
            options={
                'unique_together': {('position', 'step', 'section')},
            },
        ),
        migrations.AddField(
            model_name='step',
            name='sections',
            field=models.ManyToManyField(through='wizard.StepSection', to='wizard.Section'),
        ),
        migrations.CreateModel(
            name='SelectOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('position', models.PositiveIntegerField()),
                ('disabled', models.BooleanField(default=False)),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wizard.Option')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SectionQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('position', models.PositiveIntegerField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wizard.Question')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wizard.Section')),
            ],
            options={
                'unique_together': {('position', 'question', 'section')},
            },
        ),
        migrations.AddField(
            model_name='section',
            name='questions',
            field=models.ManyToManyField(through='wizard.SectionQuestion', to='wizard.Question'),
        ),
        migrations.CreateModel(
            name='RadioButtonOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('position', models.PositiveIntegerField()),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wizard.Option')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CheckboxOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('position', models.PositiveIntegerField()),
                ('exclusive', models.BooleanField(default=False)),
                ('required', models.BooleanField(default=False)),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wizard.Option')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MultipleChoiceField',
            fields=[
                ('jsonfield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wizard.JSONField')),
            ],
            options={
                'abstract': False,
            },
            bases=('wizard.jsonfield',),
        ),
        migrations.CreateModel(
            name='TextField',
            fields=[
                ('jsonfield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wizard.JSONField')),
                ('maxlength', models.IntegerField(blank=True, null=True)),
                ('minlength', models.IntegerField(blank=True, null=True)),
                ('pattern', models.CharField(blank=True, max_length=256, null=True)),
                ('placeholder', models.CharField(blank=True, max_length=256, null=True)),
                ('readonly', models.BooleanField(default=False)),
                ('required', models.BooleanField(default=False)),
                ('size', models.IntegerField(blank=True, null=True)),
                ('spellcheck', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('wizard.jsonfield',),
        ),
        migrations.CreateModel(
            name='Trigger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('position', models.PositiveIntegerField()),
                ('condition', models.CharField(choices=[('E', 'Value == Answer'), ('GT', 'Value > Answer'), ('GTE', 'Value >= Answer'), ('LT', 'Value < Answer'), ('LTE', 'Value <= Answer'), ('IN', 'Value in Answer')], default='E', max_length=256)),
                ('value', django.contrib.postgres.fields.jsonb.JSONField()),
                ('from_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wizard.JSONQuestion')),
                ('to_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='triggered_by', to='wizard.JSONQuestion')),
            ],
        ),
        migrations.AddField(
            model_name='jsonquestion',
            name='triggers',
            field=models.ManyToManyField(through='wizard.Trigger', to='wizard.JSONQuestion'),
        ),
        migrations.CreateModel(
            name='JSONAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('value', django.contrib.postgres.fields.jsonb.JSONField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='wizard.JSONQuestion')),
            ],
        ),
        migrations.CreateModel(
            name='FileQuestion',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wizard.Question')),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wizard.FileField')),
            ],
            options={
                'abstract': False,
            },
            bases=('wizard.question',),
        ),
        migrations.AddField(
            model_name='fileanswer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='wizard.FileQuestion'),
        ),
        migrations.CreateModel(
            name='CheckboxField',
            fields=[
                ('multiplechoicefield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wizard.MultipleChoiceField')),
            ],
            options={
                'abstract': False,
            },
            bases=('wizard.multiplechoicefield',),
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
        migrations.AddConstraint(
            model_name='trigger',
            constraint=models.CheckConstraint(check=models.Q(_negated=True, from_question=django.db.models.expressions.F('to_question')), name='trigger__different_questions'),
        ),
        migrations.AlterUniqueTogether(
            name='trigger',
            unique_together={('to_question', 'from_question', 'value', 'condition'), ('position', 'from_question', 'to_question')},
        ),
        migrations.AlterUniqueTogether(
            name='jsonanswer',
            unique_together={('question', 'user')},
        ),
        migrations.AlterUniqueTogether(
            name='fileanswer',
            unique_together={('question', 'user')},
        ),
        migrations.AddField(
            model_name='selectoption',
            name='field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wizard.SelectField'),
        ),
        migrations.AddField(
            model_name='selectfield',
            name='options',
            field=models.ManyToManyField(through='wizard.SelectOption', to='wizard.Option'),
        ),
        migrations.AddField(
            model_name='radiobuttonoption',
            name='field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wizard.RadioButtonField'),
        ),
        migrations.AddField(
            model_name='radiobuttonfield',
            name='options',
            field=models.ManyToManyField(through='wizard.RadioButtonOption', to='wizard.Option'),
        ),
        migrations.AddField(
            model_name='checkboxoption',
            name='field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wizard.CheckboxField'),
        ),
        migrations.AddField(
            model_name='checkboxfield',
            name='options',
            field=models.ManyToManyField(through='wizard.CheckboxOption', to='wizard.Option'),
        ),
        migrations.AlterUniqueTogether(
            name='selectoption',
            unique_together={('position', 'field', 'option')},
        ),
        migrations.AlterUniqueTogether(
            name='radiobuttonoption',
            unique_together={('position', 'field', 'option')},
        ),
        migrations.AlterUniqueTogether(
            name='checkboxoption',
            unique_together={('position', 'field', 'option')},
        ),
    ]
