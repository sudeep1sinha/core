# Generated by Django 5.0.1 on 2024-03-02 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_product_student_address_student_age_student_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.TextField(max_length=100)),
                ('car_speed', models.IntegerField(default=50)),
            ],
        ),
    ]
