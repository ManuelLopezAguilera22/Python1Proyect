from __future__ import annotations
from dataclasses import dataclass
from typing import Tuple
import random

@dataclass(frozen=True)
class Almacen:
    codigo: int
    nombre: str
    ciudad: str
    coordenadas: Tuple[float, float]

    @staticmethod
    def of(codigo: int, nombre: str, ciudad: str, lat: float, lon: float) -> 'Almacen':
        return Almacen(codigo, nombre, ciudad, (lat, lon))

    @staticmethod
    def parse(linea: str) -> 'Almacen':
        partes = linea.strip().split(',')
        return Almacen.of(int(partes[0]), partes[1], partes[2], float(partes[3]), float(partes[4]))

    @staticmethod
    def random() -> 'Almacen':
        ciudades = ['Sevilla', 'Madrid', 'Granada', 'Valencia']
        nombres = ['Prendas', 'Electrodomésticos', 'Herramientas', 'Juguetes']
        return Almacen.of(
            random.randint(100, 999),
            random.choice(nombres),
            random.choice(ciudades),
            round(random.uniform(-90, 90), 5),
            round(random.uniform(-180, 180), 5)
        )

    def __str__(self) -> str:
        lat, lon = self.coordenadas
        return f"{self.codigo},{self.nombre},{self.ciudad},{lat},{lon}"
