from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
User = get_user_model()


# class Command(BaseCommand):
#     help = "Генерация случаный данных в бд"
#     first_name = ["Иван", "Максим", "Татьяна", "Илья", "Григорий", "Михаил", "Герман", "Никита", "Пётр", "Степан",
#                   "Владимир", "Владимир", "Сергей", "Дмитрий", "Владислав", "Вадим", "Рустам", "Айрат", "Александр",
#                   "Артём", "Андрей", "Даниил", "Данил", "Денис", "Дарья", "Евгений", ]
#     last_name = ["Смирнов", "Кузнецов", "Попов", "Васильев", "Петров", "Семенов", "Волков", "Лебедев", "Орлов",
#                  "Морозов", "Сергеев", "Михайлов", "Михай", "ЛАБЗИН", "ЛАЗАРЕВИЧ", "ЛАВНИКОВ", "ЛАЙКОВ"]
#     orders = [
#         m.OrderStorage.objects.get_or_create(user=User, quantity=m.QuantityOfTires(pk=random("pk")))
#     ]
#     def add_arguments(self, parser):
#         parser.add_argument("--amount", type=int, help="The number of purchases that should be created.")
#
#     def handle(self, *args, **options):
#         amount = options["amount"] if options["amount"] else 2500
#
#
#         for i in range(0, amount):
#             dt = pytz.utc.localize(datetime.now() + timedelta(days=random.randint(0, 1000)))
#
#             user=m.OrderStorage.objects.create(
#                 m.OrderStorage.objects.get_or_create(user=User, quantity=m.QuantityOfTires.random.choice))
#             user.time = dt
#             user.save()
#         self.stdout.write(self.style.SUCCESS("Successfully populated the database."))


# class Command(BaseCommand):
#     help = "Генерация случаный данных в бд"
#     first_name = ["Иван", "Максим", "Татьяна", "Илья", "Григорий", "Михаил", "Герман", "Никита", "Пётр", "Степан",
#                   "Владимир", "Владимир", "Сергей", "Дмитрий", "Владислав", "Вадим", "Рустам", "Айрат", "Александр",
#                   "Артём", "Андрей", "Даниил", "Данил", "Денис", "Дарья", "Евгений", ]
#     last_name = ["Смирнов", "Кузнецов", "Попов", "Васильев", "Петров", "Семенов", "Волков", "Лебедев", "Орлов",
#                  "Морозов", "Сергеев", "Михайлов", "Михай", "ЛАБЗИН", "ЛАЗАРЕВИЧ", "ЛАВНИКОВ", "ЛАЙКОВ"]
#
#     def add_arguments(self, parser):
#         parser.add_argument("--amount", type=int, help="The number of purchases that should be created.")
#
#     def handle(self, *args, **options):
#         amount = options["amount"] if options["amount"] else 2500
#
#
#         for i in range(0, amount):
#             dt = pytz.utc.localize(datetime.now() + timedelta(days=random.randint(0, 1000)))
#             first = random.choice(self.first_name)
#             last = random.choice(self.last_name)
#             username = first + last + str(random.randint(-900, 900))
#             email = first + last + "@example.com"
#             password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
#             user = User.objects.create(
#                 first_name=first,
#                 last_name=last,
#                 username=username,
#                 email=email,
#                 password=make_password(password),)
#             user.time = dt
#             user.save()
#         self.stdout.write(self.style.SUCCESS("Successfully populated the database."))

from faker import Faker


class Command(BaseCommand):
    help = 'Generate 1000 unique users'

    def handle(self, *args, **options):
        fake = Faker('ru_RU')
        for _ in range(1000):
            first_name = fake.first_name()
            last_name = fake.last_name()
            middle_name = fake.middle_name()
            phone_number = fake.phone_number()
            email = fake.email()

            username = f"{first_name.lower()}.{last_name.lower()}"

            # Ensure the generated username is unique
            while User.objects.filter(username=username).exists():
                username = f"{first_name.lower()}.{last_name.lower()}.{fake.random_number(digits=3)}"

            User.objects.create_user(
                username=username,
                password=fake.password(),
                first_name=first_name,
                last_name=last_name,
                email=email,
            )
