from django.core.management.base import BaseCommand, CommandError
from backend.Controladores.ControladorUsuarios import ControladorUsuarios
from backend.modelsApp import Usuario
#from django.utils.timezone import ti

class Command(BaseCommand):
    help = 'Crea usuario administrador en caso de que no existan usuarios'
    def add_arguments(self, parser):
        parser.add_argument('password', nargs='+', type=str)
    
    def handle(self, *args, **options):
        if 'password' in options:
            try:
                res = ControladorUsuarios.ListarUsuarios()
                if isinstance(res, list):
                    if len(res) == 0:
                        usrAdmin = Usuario(rut="1-1", user="adminTemp999", nombres="Administrador", apellidos="", password=options['password'][0], vigencia=True, administrador=True)
                        res = ControladorUsuarios.AgregarUsuario(usrAdmin)
                        if res.CodigoOperacion != 200:
                            raise CommandError('Error al ingresar el usuario: ' + res.Mensaje)
                        else:
                            self.stdout.write(self.style.SUCCESS('Usuario administrador agregado con nombre de usuario "adminTemp999"'))
                    else:
                        raise CommandError('Ya existe un usuario administrador')
                else:
                    raise CommandError('Error al obtener usuarios: ' + res.Mensaje)
            except Exception as ex:
                raise CommandError('Error: ' + str(ex))