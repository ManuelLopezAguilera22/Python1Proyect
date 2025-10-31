'''
Created on 29 sept 2025

@author: belenvegmar
'''

import unittest
import datetime
from math import factorial

from src.entrega1.Funciones import *


class TestEjercicio1(unittest.TestCase):
    def test_fecha_valida_normal(self):
        self.assertTrue(es_fecha_valida(15, 3, 2025))  # sábado

    def test_fecha_invalida_no_existe(self):
        self.assertFalse(es_fecha_valida(31, 2, 2025))  # febrero no tiene 31

    def test_fecha_invalida_domingo(self):
        self.assertFalse(es_fecha_valida(28, 9, 2025))  # domingo

    def test_fecha_bisiesto_valida(self):
        self.assertTrue(es_fecha_valida(29, 2, 2024))  # año bisiesto

    def test_fecha_bisiesto_invalida(self):
        self.assertFalse(es_fecha_valida(29, 2, 2023))  # año no bisiesto


class TestEjercicio2(unittest.TestCase):
    def test_producto_basico(self):
        self.assertEqual(producto(4, 2), 20)


    def test_producto_error(self):
        with self.assertRaises(AssertionError):
            producto(3, 5)


class TestEjercicio3(unittest.TestCase):
    def test_sucesion_geom_basica(self):
        self.assertEqual(secuencia_geom(3, 5, 2), 45)



class TestEjercicio4(unittest.TestCase):
    def test_combinatorio_basico(self):
        self.assertEqual(combinatorio(4, 2), 6)

    def test_combinatorio_borde(self):
        self.assertEqual(combinatorio(5, 0), 1)
        self.assertEqual(combinatorio(5, 5), 1)

    def test_combinatorio_error(self):
        with self.assertRaises(AssertionError):
            combinatorio(3, 5)


class TestEjercicio5(unittest.TestCase):
    def test_snk_basico(self):
        self.assertEqual(SNK(4, 2), 22.5)


    def test_snk_error(self):
        with self.assertRaises(AssertionError):
            SNK(2, 5)


if __name__ == "__main__":
    unittest.main()
    