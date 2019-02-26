import unittest
import funciones as f

class pruebas(unittest.TestCase):

    def test_calcular_precio_producto(self):
        self.assertEqual(f.calcular_precio_producto(1000), 1500)
        self.assertEqual(f.calcular_precio_producto(0), 0)

    def test_calcular_precio_servicio(self):
        self.assertEqual(f.calcular_precio_servicio(2), 200000)
        self.assertEqual(f.calcular_precio_servicio(0), 0)

    def test_calcular_precio_servicio_extras(self):
        self.assertEqual(f.calcular_precio_servicio_extras(2), 250000)
        self.assertEqual(f.calcular_precio_servicio_extras(0), 0)

    def test_calcular_costo_envio(self):
        self.assertEqual(f.calcular_costo_envio(1000), 115000)
        self.assertEqual(f.calcular_costo_envio(0), 0)

    def test_calcular_precio_producto_fuera(self):
        self.assertEqual(f.calcular_precio_producto_fuera(1000,2), 1730)
        self.assertEqual(f.calcular_precio_producto_fuera(0,0), 0)

    def test_calcular_iva_producto(self):
        self.assertEqual(f.calcular_iva_producto(1000,19.0), 285)

    def test_calcular_iva_servicio(self):
        self.assertEqual(f.calcular_iva_servicio(1,19.0), 19000)

    def test_calcular_iva_envio(self):
        self.assertEqual(f.calcular_iva_envio(1, 19.0), 21.85)

    def test_calcular_iva_servicio_fuera(self):
        self.assertEqual(f.calcular_iva_servicio_extra(1, 19.0), 23750)


    def test_calcular_recaudo_locales(self):
        self.assertEqual(f.calcular_recaudo_locales(100,200,300),900)


    def test_calcular_recaudo_horas_extra(self):
        self.assertEqual(f.calcular_recaudo_horas_extra(1,2,3,4),1250000)

    def test_calcular_recaudo_mixto_local(self):
        self.assertEqual(f.calcular_recaudo_mixto_local(100,200,1,2),375450)


if __name__ == 'main':
    unittest.main()
