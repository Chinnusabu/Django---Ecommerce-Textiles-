# Generated by Django 5.0.7 on 2024-08-21 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TextWebApp', '0004_createaccountdb_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Product_Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Quantity', models.IntegerField(blank=True, null=True)),
                ('Price', models.IntegerField(blank=True, null=True)),
                ('Total_Price', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
