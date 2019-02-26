
def calcular_precio_producto(coste_producto):
    return coste_producto + (coste_producto*0.5)


def calcular_precio_servicio(cantidad_horas):
    return cantidad_horas * 100000


def calcular_precio_servicio_extras(cantidad_horas):
    tarifa = calcular_precio_servicio(cantidad_horas)
    return tarifa + (tarifa*0.25)


def calcular_costo_envio(kilometros):
    return kilometros *115

def calcular_precio_producto_fuera(coste_producto,
                                   kilometros):
    return calcular_precio_producto(coste_producto) +calcular_costo_envio(kilometros)


def calcular_iva_producto(coste_producto, tasa):
    return calcular_precio_producto(coste_producto) * (tasa/100)


def calcular_iva_servicio(cantidad_horas, tasa):
    return calcular_precio_servicio(cantidad_horas) * (tasa/100)


def calcular_iva_envio(kilometros, tasa):
    return calcular_costo_envio(kilometros) * (tasa/100)


def calcular_iva_servicio_extra(cantidad_horas, tasa):
    return calcular_precio_servicio_extras(cantidad_horas)  * (tasa/100)


def calcular_recaudo_locales(coste_producto_1,
                             coste_producto_2,
                             coste_producto_3):
    return calcular_precio_producto(coste_producto_1) + calcular_precio_producto(coste_producto_2) + calcular_precio_producto(coste_producto_3)

def calcular_recaudo_horas_extra(horas_1,
                                 horas_2,
                                 horas_3,
                                 horas_4):
    return calcular_precio_servicio_extras(horas_1) + calcular_precio_servicio_extras(horas_2) + calcular_precio_servicio_extras(horas_3) + calcular_precio_servicio_extras(horas_4)


def calcular_recaudo_mixto_local(coste_producto_1,
                                 coste_producto_2,
                                 horas_1,
                                 horas_2):
    return calcular_precio_producto(coste_producto_1) + calcular_precio_producto(coste_producto_2) + calcular_precio_servicio_extras(horas_1) + calcular_precio_servicio_extras(horas_2)