from django.core.management.base import BaseCommand
from accounts.models import Usuario

class Command(BaseCommand):
    help = 'Crear usuarios con diferentes roles'

    def handle(self, *args, **kwargs):
        gerente = Usuario.objects.create_user(
            username="andy",
            email="gerente@gmail.com",
            password="54321",
            rol="Gerente"
        )
        self.stdout.write(f"Usuario creado: {gerente.email}, Rol: {gerente.rol}")

        contador = Usuario.objects.create_user(
            username="angelo",
            email="contador@gmail.com",
            password="56789",
            rol="Contador"
        )
        self.stdout.write(f"Usuario creado: {contador.email}, Rol: {contador.rol}")
