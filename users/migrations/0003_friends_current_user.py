# Generated by Django 2.1.3 on 2018-11-10 04:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_friends'),
    ]

    operations = [
        migrations.AddField(
            model_name='friends',
            name='current_user',
            field=models.ForeignKey(null=True, on_delete=None, related_name='owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
