# Generated by Django 5.0.3 on 2024-04-05 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Portal', '0003_alter_user_email_alter_user_has_company_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]