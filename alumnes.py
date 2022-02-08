
from datetime import datetime


def orden_nombre(lista):
    pass
    #lista.sort(key=lambda x: x['alumne'])
    return str(lista)


def orden_data(lista):
    lista.sort(key=lambda x: datetime.strptime(x['data_naiximent'],'%d-%m-%Y'))
    return str(lista)
