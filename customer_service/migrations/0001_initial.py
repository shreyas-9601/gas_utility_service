# Generated by Django 5.1.3 on 2024-11-18 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('service_type', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('attached_file', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Resolved', 'Resolved')], default='Pending', max_length=20)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('resolved_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
