# Generated by Django 5.1.4 on 2025-01-16 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_reservation_children_room_discount_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='children',
        ),
    ]
