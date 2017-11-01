# Generated by Django 2.1 on 2017-10-22 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_diplom_songoson'),
    ]

    operations = [
        migrations.CreateModel(
            name='plan',
            fields=[
                ('date', models.DateTimeField(auto_now_add=True)),
                ('plan_id', models.AutoField(primary_key=True, serialize=False)),
                ('topic', models.CharField(max_length=255)),
                ('note', models.CharField(max_length=2000)),
                ('start_date', models.DateField()),
                ('start_time', models.TimeField(null=True)),
                ('finish_date', models.DateField()),
                ('finish_time', models.TimeField(null=True)),
            ],
        ),
    ]