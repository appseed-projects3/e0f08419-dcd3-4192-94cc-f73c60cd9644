# Generated by Django 3.2.13 on 2022-06-07 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_user', '0002_user_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(db_index=True, max_length=255, unique=True),
        ),
    ]