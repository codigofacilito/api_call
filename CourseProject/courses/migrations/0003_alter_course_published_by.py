# Generated by Django 4.2.11 on 2024-04-20 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_course_published_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='published_by',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
