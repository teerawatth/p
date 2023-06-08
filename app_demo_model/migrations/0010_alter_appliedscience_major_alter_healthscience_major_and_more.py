# Generated by Django 4.1.6 on 2023-02-13 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_demo_model', '0009_alter_appliedscience_admission_grade_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appliedscience',
            name='major',
            field=models.CharField(choices=[('bio', 'ชีววิทยา'), ('microBio', 'จุลชีววิทยา'), ('math', 'คณิตศาสตร์'), ('chemi', 'เคมี'), ('enviSci', 'วิทยศาสตร์สิ่งแวดล้อม'), ('safety', 'อนามัยสิ่งแวดล้อมและความปลอดภัย'), ('physics', 'ฟิสิกส์'), ('physics', 'ฟิสิกส์ทางการแพทย์'), ('physics', 'ฟิสิกส์อุตสาหกรรม'), ('ICT', 'เทคโนโลยีสารสนเทศ'), ('ICT', 'เทคโนโลยีและการสื่อสาร'), ('DSSI', 'วิทยาการคอมพิวเตอร์'), ('DSSI', 'วิทยาการข้อมูลและนวัตกรรมซอฟต์แวร์'), ('polymer', 'เทคโนโลยีการยางและพอลิเมอร์')], max_length=100),
        ),
        migrations.AlterField(
            model_name='healthscience',
            name='major',
            field=models.CharField(choices=[('bio', 'ชีววิทยา'), ('microBio', 'จุลชีววิทยา'), ('math', 'คณิตศาสตร์'), ('chemi', 'เคมี'), ('enviSci', 'วิทยศาสตร์สิ่งแวดล้อม'), ('safety', 'อนามัยสิ่งแวดล้อมและความปลอดภัย'), ('physics', 'ฟิสิกส์'), ('physics', 'ฟิสิกส์ทางการแพทย์'), ('physics', 'ฟิสิกส์อุตสาหกรรม'), ('ICT', 'เทคโนโลยีสารสนเทศ'), ('ICT', 'เทคโนโลยีและการสื่อสาร'), ('DSSI', 'วิทยาการคอมพิวเตอร์'), ('DSSI', 'วิทยาการข้อมูลและนวัตกรรมซอฟต์แวร์'), ('polymer', 'เทคโนโลยีการยางและพอลิเมอร์')], max_length=100),
        ),
        migrations.AlterField(
            model_name='purescience',
            name='major',
            field=models.CharField(choices=[('bio', 'ชีววิทยา'), ('microBio', 'จุลชีววิทยา'), ('math', 'คณิตศาสตร์'), ('chemi', 'เคมี'), ('enviSci', 'วิทยศาสตร์สิ่งแวดล้อม'), ('safety', 'อนามัยสิ่งแวดล้อมและความปลอดภัย'), ('physics', 'ฟิสิกส์'), ('physics', 'ฟิสิกส์ทางการแพทย์'), ('physics', 'ฟิสิกส์อุตสาหกรรม'), ('ICT', 'เทคโนโลยีสารสนเทศ'), ('ICT', 'เทคโนโลยีและการสื่อสาร'), ('DSSI', 'วิทยาการคอมพิวเตอร์'), ('DSSI', 'วิทยาการข้อมูลและนวัตกรรมซอฟต์แวร์'), ('polymer', 'เทคโนโลยีการยางและพอลิเมอร์')], max_length=100),
        ),
    ]
