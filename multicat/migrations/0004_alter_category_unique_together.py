# Generated by Django 3.2.4 on 2021-06-30 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('multicat', '0003_auto_20210630_1022'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='category',
            unique_together={('parent', 'c_name')},
        ),
    ]
