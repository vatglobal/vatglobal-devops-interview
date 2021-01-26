# Generated by Django 2.1.3 on 2018-12-19 08:07
import sys

from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.db import migrations, IntegrityError, transaction


def add_default_user(apps, schema_editor):
    username = 'admin'
    email = 'devops@vatglobal.local'
    password = 'W1thGreatResponsibility'
    User = apps.get_model(settings.AUTH_USER_MODEL)

    try:
        with transaction.atomic():
            admin = User(
                username=username,
                email=email,
                password=make_password(password),
                is_superuser=True,
                is_staff=True
            )
            admin.save()
    except IntegrityError:
        sys.stdout.write(" User '%s <%s>' already exists..." % (username, email))
    else:
        sys.stdout.write(" Created superuser '%s <%s>' with password '%s'!" % (username, email, password))


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RunPython(add_default_user)
    ]
