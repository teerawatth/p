# Generated by Django 4.1.6 on 2023-02-04 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_demo_model', '0002_appliedscimodelforperdiction_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AppliedSciModelForPerdiction',
        ),
        migrations.DeleteModel(
            name='HealthSciModelForPerdiction',
        ),
        migrations.DeleteModel(
            name='PureSciModelForPerdiction',
        ),
        migrations.AlterField(
            model_name='purescience',
            name='admission_grade',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='purescience',
            name='art',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='purescience',
            name='career',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='purescience',
            name='gpa_year_1',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='purescience',
            name='hygiene',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='purescience',
            name='langues',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='purescience',
            name='major',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='purescience',
            name='math',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='purescience',
            name='sci',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='purescience',
            name='society',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='purescience',
            name='status',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='purescience',
            name='thai',
            field=models.CharField(max_length=5),
        ),
    ]
