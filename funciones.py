


def calcular_precio_producto(coste_producto):
    """
    Calcula el precio producto con 50 % sobre costo
    :param coste_producto: valor producto
    :return: float resultante con precio con 50 %
    """
    return coste_producto + (coste_producto * 0.5)


def calcular_precio_servicio(cantidad_horas):
    """
    valor hora extra
    :param cantidad_horas: representa cantidad horas extras
    :return: valor de la hora extra
    """
    return cantidad_horas * 100000


def calcular_precio_servicio_extras(cantidad_horas):
    """
    calcula el valor de la hora extra
    :param cantidad_horas: cantidad horas extras
    :return:  float valor de la tarifa hora extra
    """
    tarifa = calcular_precio_servicio(cantidad_horas)
    return tarifa + (tarifa * 0.25)


def calcular_costo_envio(kilometros):
    """
    esta funcion calcula el costo del envio segun el numero de kilometro fuera de la ciudad
    :param kilometros: Int representa la cantidad de kilometros
    :return: valor del kilometro
    """
    return kilometros * 115


def calcular_precio_producto_fuera(coste_producto,
                                   kilometros):
    """
    calcula el costo del producto con la tarifa por kilometro fuera de la ciudad
    :param coste_producto: float valor producto con 50 %
    :param kilometros: cantidad de kilometro fuera de la ciudad
    :return: float valor del producto fuera de la ciudad
    """
    return calcular_precio_producto(coste_producto) + calcular_costo_envio(kilometros)


def calcular_iva_producto(coste_producto, tasa):
    """
    esta funcion calcula los productos con iva si es persona juridica
    :param coste_producto:  float  valor del producto
    :param tasa: float 19 %
    :return: costo del producto con iva
    """
    return calcular_precio_producto(coste_producto) * (tasa / 100)


def calcular_iva_servicio(cantidad_horas, tasa):
    """
    calcula el precio del servicio con iva
    :param cantidad_horas: int cantidad horas
    :param tasa: float 19 %
    :return: valor hora servicio con iva
    """
    return calcular_precio_servicio(cantidad_horas) * (tasa / 100)


def calcular_iva_envio(kilometros, tasa):
    """
    esta funcion calcula el valor del envio con iva
    :param kilometros: int cantidad de kilometros
    :param tasa: float 19 %
    :return: costo del envio con iva
    """
    return calcular_costo_envio(kilometros) * (tasa / 100)


def calcular_iva_servicio_extra(cantidad_horas, tasa):
    """
    esta funcion calcula el valor del iva de un servicio extra
    :param cantidad_horas: int cantidad horas
    :param tasa: float 19 %
    :return: valor iva de un servicio extra
    """
    return calcular_precio_servicio_extras(cantidad_horas) * (tasa / 100)


def calcular_recaudo_locales(coste_producto_1,
                             coste_producto_2,
                             coste_producto_3):
    """
    recaudo de tres productos
    :param coste_producto_1: float valor producto 1
    :param coste_producto_2: float valor producto 2
    :param coste_producto_3: float valor producto 3
    :return: el total del recaudo
    """
    return calcular_precio_producto(coste_producto_1) + calcular_precio_producto(
        coste_producto_2) + calcular_precio_producto(coste_producto_3)


def calcular_recaudo_horas_extra(horas_1,
                                 horas_2,
                                 horas_3,
                                 horas_4):
    """
    recaudo valor hora extras
    :param horas_1: float valor hora extra hora_1
    :param horas_2: float valor hora extra hora_2
    :param horas_3: float valor hora extra hora_3
    :param horas_4: float valor hora extra hora_4
    :return: total del recaudo horas extra
    """
    return calcular_precio_servicio_extras(horas_1) + calcular_precio_servicio_extras(
        horas_2) + calcular_precio_servicio_extras(horas_3) + calcular_precio_servicio_extras(horas_4)


def calcular_recaudo_mixto_local(coste_producto_1,
                                 coste_producto_2,
                                 horas_1,
                                 horas_2):
    """
    recaudo de productos y servicios
    :param coste_producto_1: valor producto_1
    :param coste_producto_2: valor producto_2
    :param horas_1: valor horas_1
    :param horas_2: valor horas_2
    :return: recaudo total productos y servicios
    """
    return calcular_precio_producto(coste_producto_1) + calcular_precio_producto(
        coste_producto_2) + calcular_precio_servicio_extras(horas_1) + calcular_precio_servicio_extras(horas_2)
