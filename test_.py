import alumnes
import datos


def test1():
    assert alumnes.orden_nombre(datos.students) == str(datos.students_orden_nom)

def test2():
    assert alumnes.orden_data(datos.students) == str(datos.students_orden_data)
