# Generated by Django 3.0.3 on 2020-10-09 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.CharField(max_length=200)),
                ('Option1', models.CharField(max_length=200)),
                ('Option2', models.CharField(max_length=200)),
                ('Option3', models.CharField(max_length=200)),
                ('Option4', models.CharField(max_length=200)),
            ],
        ),
    ]
