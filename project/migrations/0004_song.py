# Generated by Django 4.0.5 on 2022-07-05 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]