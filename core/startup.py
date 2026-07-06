from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


def create_admin():
    username = settings.ADMIN_USERNAME
    email = settings.ADMIN_EMAIL
    password = settings.ADMIN_PASSWORD

    if not username or not password:
        return

    if not User.objects.filter(username=username).exists():
        print("Creating admin user...")

        User.objects.create_superuser(
            username=username,
            email=email,
            password=password,
        )

        print("Admin user created.")