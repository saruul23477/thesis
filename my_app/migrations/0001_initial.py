# Generated by Django 2.1 on 2017-10-16 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='detail',
            fields=[
                ('date', models.DateTimeField(auto_now_add=True)),
                ('detail_id', models.AutoField(primary_key=True, serialize=False)),
                ('tch_id', models.CharField(max_length=140)),
                ('dip', models.BooleanField(default=False)),
                ('tos', models.BooleanField(default=False)),
                ('dun', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='diplom',
            fields=[
                ('d_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('topic', models.CharField(max_length=255)),
                ('note', models.CharField(max_length=2000)),
                ('check', models.BooleanField(default=False)),
                ('now', models.BooleanField(default=False)),
                ('tosol', models.BooleanField(default=False)),
                ('diplom', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='research',
            fields=[
                ('res_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('topic', models.CharField(max_length=255)),
                ('note', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('mail', models.CharField(max_length=140)),
                ('lname', models.CharField(max_length=140)),
                ('fname', models.CharField(max_length=140)),
                ('code', models.CharField(max_length=25, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=140)),
                ('degree', models.CharField(max_length=140, null=True)),
                ('phone', models.CharField(max_length=140, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='my_app/static/avatar/')),
                ('erhlegch', models.BooleanField(default=False)),
                ('nariin', models.BooleanField(default=False)),
                ('dip', models.BooleanField(default=False)),
                ('tos', models.BooleanField(default=False)),
                ('songoson', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='research',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.users'),
        ),
        migrations.AddField(
            model_name='diplom',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.users'),
        ),
        migrations.AddField(
            model_name='detail',
            name='d_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.diplom'),
        ),
        migrations.AddField(
            model_name='detail',
            name='st_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.users'),
        ),
    ]
