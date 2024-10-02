# Generated by Django 5.0.7 on 2024-08-26 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TextWebApp', '0005_cartdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Email', models.EmailField(blank=True, max_length=50, null=True)),
                ('Mobile', models.IntegerField(blank=True, null=True)),
                ('Address', models.TextField(blank=True, max_length=500, null=True)),
                ('City', models.CharField(blank=True, max_length=50, null=True)),
                ('Message', models.TextField(blank=True, max_length=500, null=True)),
                ('Total_Amount', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='createaccountdb',
            name='Password',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
