# Generated by Django 3.0.5 on 2020-04-29 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('adresse', models.TextField()),
                ('photo', models.ImageField(upload_to='photos/')),
            ],
        ),
    ]
