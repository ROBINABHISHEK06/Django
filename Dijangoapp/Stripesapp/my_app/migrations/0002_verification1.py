# Generated by Django 5.0.3 on 2024-04-08 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Verification1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificateCourse', models.CharField(max_length=100)),
                ('certificateNo', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('courseName', models.CharField(max_length=100)),
                ('certificateStripes', models.CharField(max_length=100)),
                ('participantName', models.CharField(max_length=100)),
                ('passportNo', models.CharField(max_length=100)),
                ('courseDate1', models.DateField()),
                ('courseDate2', models.DateField()),
                ('issueDate', models.DateField()),
            ],
        ),
    ]
