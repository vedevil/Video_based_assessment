# Generated by Django 4.2.4 on 2023-08-27 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionPack',
            fields=[
                ('org_id', models.CharField(max_length=50)),
                ('access_id', models.IntegerField(primary_key=True, serialize=False)),
                ('access_status', models.BooleanField(default=True)),
                ('s_no', models.IntegerField(default=1)),
                ('unique_id', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('summary', models.TextField()),
                ('max_attempts', models.PositiveIntegerField()),
                ('min_response_duration', models.PositiveIntegerField()),
                ('max_response_duration', models.PositiveIntegerField()),
                ('submit_screen_title', models.CharField(max_length=100)),
                ('submit_screen_message', models.TextField()),
                ('show_question_numbers', models.BooleanField()),
                ('feedback_url', models.URLField()),
                ('feedback_message', models.TextField()),
                ('feedback_button_text', models.CharField(max_length=50)),
                ('expiration_timestamp', models.BigIntegerField()),
                ('end_timestamp', models.BigIntegerField()),
                ('ended_message', models.TextField()),
                ('require_linkedin', models.BooleanField()),
                ('linkedin_username', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_id', models.CharField(max_length=50)),
                ('ques_id', models.IntegerField()),
                ('ques_text', models.TextField()),
                ('ques_type', models.CharField(max_length=50)),
                ('access_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video_interview.questionpack')),
            ],
        ),
    ]