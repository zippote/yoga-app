# Generated by Django 3.2.8 on 2021-10-10 14:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teachers', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('lessons', models.IntegerField()),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('start_date', models.DateField(blank=True, default=datetime.date.today)),
                ('main_pic', models.ImageField(upload_to='photos/%Y/m/%d/')),
                ('pic_1', models.ImageField(blank=True, upload_to='photos/%Y/m/%d/')),
                ('pic_2', models.ImageField(blank=True, upload_to='photos/%Y/m/%d/')),
                ('pic_3', models.ImageField(blank=True, upload_to='photos/%Y/m/%d/')),
                ('is_published', models.BooleanField(default=True)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='teachers.teacher')),
            ],
        ),
    ]
