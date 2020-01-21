# Generated by Django 2.2.7 on 2020-01-15 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bugz', '0005_user_is_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='mobile_no',
            field=models.IntegerField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
