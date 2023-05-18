import random
from faker import Faker
from django.contrib.auth.models import User

def generate_unique_users():
    fake = Faker()
    users = []
    for _ in range(1000):
        first_name = fake.first_name()
        last_name = fake.last_name()
        middle_name = fake.first_name()
        phone_number = fake.phone_number()
        email = fake.email()

        username = f"{first_name.lower()}.{last_name.lower()}"
        password = fake.password()

        # Ensure the generated username is unique
        while User.objects.filter(username=username).exists():
            username = f"{first_name.lower()}.{last_name.lower()}.{random.randint(1, 1000)}"

        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
        )
        user.middle_name = middle_name
        user.phone_number = phone_number
        user.save()
        users.append(user)

    return users
