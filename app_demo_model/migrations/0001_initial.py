# Generated by Django 4.1.5 on 2023-01-17 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppliedScience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major', models.CharField(max_length=100)),
                ('admission_grade', models.CharField(max_length=5)),
                ('gpa_year_1', models.CharField(max_length=5)),
                ('thai', models.CharField(max_length=5)),
                ('math', models.CharField(max_length=5)),
                ('sci', models.CharField(max_length=5)),
                ('society', models.CharField(max_length=5)),
                ('hygiene', models.CharField(max_length=5)),
                ('art', models.CharField(max_length=5)),
                ('career', models.CharField(max_length=5)),
                ('langues', models.CharField(max_length=5)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='HealthScience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major', models.CharField(max_length=100)),
                ('admission_grade', models.CharField(max_length=5)),
                ('gpa_year_1', models.CharField(max_length=5)),
                ('thai', models.CharField(max_length=5)),
                ('math', models.CharField(max_length=5)),
                ('sci', models.CharField(max_length=5)),
                ('society', models.CharField(max_length=5)),
                ('hygiene', models.CharField(max_length=5)),
                ('art', models.CharField(max_length=5)),
                ('career', models.CharField(max_length=5)),
                ('langues', models.CharField(max_length=5)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PureScience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major', models.CharField(max_length=100)),
                ('admission_grade', models.CharField(max_length=5)),
                ('gpa_year_1', models.CharField(max_length=5)),
                ('thai', models.CharField(max_length=5)),
                ('math', models.CharField(max_length=5)),
                ('sci', models.CharField(max_length=5)),
                ('society', models.CharField(max_length=5)),
                ('hygiene', models.CharField(max_length=5)),
                ('art', models.CharField(max_length=5)),
                ('career', models.CharField(max_length=5)),
                ('langues', models.CharField(max_length=5)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
    ]