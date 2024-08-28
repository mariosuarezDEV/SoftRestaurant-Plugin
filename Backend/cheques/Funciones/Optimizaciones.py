from datetime import datetime

from cheques.models import Cheques, Cheqdet

# Funcion para obtener solo los cheques de la fecha en la que se abre la pagina

class optimizaciones:
    def __init__(self):
        pass

    def get_cheques_loading(self):
        # Obtener la fecha actual INCIO(año - mes - dia 00:00:00) FIN(año - mes - dia 23:59:59)
        fecha_actual_inicio = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        fecha_actual_fin = datetime.now().replace(hour=23, minute=59, second=59, microsecond=0)
        # Obtener los cheques de la fecha actual
        try:
            cheques = Cheques.objects.filter(fecha__range=(fecha_actual_inicio, fecha_actual_fin))
            return cheques
        except Exception as e:
            return e

    def get_cheques_detalles_fecha_inicio(self, fecha_inicio):
        # Establecer la hora de inicio y fin del día
        fecha_actual_inicio = fecha_inicio.replace(hour=0, minute=0, second=0, microsecond=0)
        fecha_actual_fin = fecha_inicio.replace(hour=23, minute=59, second=59, microsecond=0)
        try:
            # Obtener los cheques de la fecha actual
            cheques = Cheques.objects.filter(fecha__range=(fecha_actual_inicio, fecha_actual_fin))
            return cheques
        except Exception as e:
            return str(e)

    def get_cheques_fechas(self, fecha_inicio, fecha_fin):
        # Establecer la hora de inicio y fin del día
        fecha_actual_inicio = fecha_inicio.replace(hour=0, minute=0, second=0, microsecond=0)
        fecha_actual_fin = fecha_fin.replace(hour=23, minute=59, second=59, microsecond=0)
        try:
            # Obtener los cheques de la fecha actual
            cheques = Cheques.objects.filter(fecha__range=(fecha_actual_inicio, fecha_actual_fin))
            return cheques
        except Exception as e:
            return str(e)