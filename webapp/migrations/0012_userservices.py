# Generated by Django 4.2 on 2023-10-05 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_servicesmodel_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='userservices',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sid', models.IntegerField()),
                ('pic', models.ImageField(upload_to='uploads/')),
                ('title', models.TextField(null=True)),
                ('Name', models.CharField(max_length=100)),
                ('Phone', models.CharField(max_length=55)),
                ('Email', models.EmailField(max_length=254)),
                ('Address', models.CharField(max_length=100)),
                ('Message', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'usersertb',
            },
        ),
    ]
