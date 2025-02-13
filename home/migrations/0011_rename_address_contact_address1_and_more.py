# Generated by Django 5.1.4 on 2025-01-16 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_privacypolicy_termsofservice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='address',
            new_name='address1',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='email',
            new_name='email1',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='phone',
            new_name='phone1',
        ),
        migrations.AddField(
            model_name='contact',
            name='address2',
            field=models.CharField(blank=True, max_length=225),
        ),
        migrations.AddField(
            model_name='contact',
            name='email2',
            field=models.CharField(blank=True, max_length=225),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone2',
            field=models.CharField(blank=True, max_length=225),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone3',
            field=models.CharField(blank=True, max_length=225),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone4',
            field=models.CharField(blank=True, max_length=225),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone5',
            field=models.CharField(blank=True, max_length=225),
        ),
    ]
