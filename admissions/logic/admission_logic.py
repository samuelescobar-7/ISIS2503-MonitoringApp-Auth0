from ..models import Admission


def get_admissions():
    """
    Retorna todas las instancias de Admission.
    """
    queryset = Admission.objects.all()
    return queryset


def get_admission(id):
    """
    Obtiene una instancia de Admission por su ID usando una consulta raw.
    """
    # Asegúrate de que el nombre de la tabla corresponda al de tu app (admissions_admission es el nombre por defecto)
    admission = Admission.objects.raw(
        "SELECT * FROM admissions_admission WHERE id=%s" % id
    )[0]
    return admission


def create_admission(form):
    """
    Crea una nueva Admission a partir de un formulario válido y la guarda en la base de datos.
    """
    admission = form.save()
    admission.save()
    # No retornamos nada (siguiendo el patrón de create_variable)
    return ()
