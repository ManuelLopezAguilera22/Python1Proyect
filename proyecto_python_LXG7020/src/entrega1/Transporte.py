from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import Enum
import random

class Periodicidad(Enum):
    DAILY = 'DAILY'
    WEEKLY = 'WEEKLY'
    MONTHLY = 'MONTHLY'

@dataclass(frozen=True)
class Transporte:
    al1: int
    al2: int
    fecha: datetime
    preparacion: int
    duracion: int
    periodicidad: Periodicidad
    dia_semana: int = None
    dia_mes: int = None

    @staticmethod
    def of(al1, al2, fecha, prep, dur, periodicidad, dia_semana=None, dia_mes=None):
        return Transporte(al1, al2, fecha, prep, dur, periodicidad, dia_semana, dia_mes)

    @staticmethod
    def parse(linea: str) -> 'Transporte':
        partes = linea.strip().split(',')
        al1 = int(partes[0])
        al2 = int(partes[1])
        fecha = datetime.strptime(partes[2], "%Y-%m-%d %H:%M")
        preparacion = int(partes[3])
        duracion = int(partes[4])
        periodicidad = Periodicidad[partes[5]]

        dia_semana = None
        dia_mes = None

        if periodicidad == Periodicidad.WEEKLY and len(partes) > 6:
            dia_semana = int(partes[6])
        elif periodicidad == Periodicidad.MONTHLY and len(partes) > 6:
            dia_mes = int(partes[6])

        return Transporte.of(al1, al2, fecha, preparacion, duracion, periodicidad, dia_semana, dia_mes)

    @staticmethod
    def random() -> 'Transporte':
        periodicidad = random.choice(list(Periodicidad))
        fecha = datetime.now().replace(hour=random.randint(0, 23), minute=random.randint(0, 59))
        dia_semana = random.randint(0, 6) if periodicidad == Periodicidad.WEEKLY else None
        dia_mes = random.randint(1, 28) if periodicidad == Periodicidad.MONTHLY else None
        return Transporte.of(
            random.randint(1, 100),
            random.randint(1, 100),
            fecha,
            random.randint(10, 60),
            random.randint(60, 180),
            periodicidad,
            dia_semana,
            dia_mes
        )

    def siguiente_fecha_disponible(self, f: datetime) -> tuple[datetime, datetime]:
        salida = self._calcular_salida(f)
        llegada = salida + timedelta(minutes=self.duracion)
        return salida, llegada

    def _calcular_salida(self, f: datetime) -> datetime:
        base = f + timedelta(minutes=self.preparacion)
        hora_transporte = self.fecha.time()

        if self.periodicidad == Periodicidad.DAILY:
            salida = base.replace(hour=hora_transporte.hour, minute=hora_transporte.minute)
            if salida <= base:
                salida += timedelta(days=1)
            return salida

        elif self.periodicidad == Periodicidad.WEEKLY:
            dias_a_sumar = (self.dia_semana - base.weekday() + 7) % 7
            salida = base + timedelta(days=dias_a_sumar)
            return salida.replace(hour=hora_transporte.hour, minute=hora_transporte.minute)

        elif self.periodicidad == Periodicidad.MONTHLY:
            mes = base.month + (1 if base.day >= self.dia_mes else 0)
            año = base.year + (mes - 1) // 12
            mes = (mes - 1) % 12 + 1
            salida = datetime(año, mes, self.dia_mes, hora_transporte.hour, hora_transporte.minute)
            return salida

    def __str__(self):
        return f"{self.al1},{self.al2},{self.fecha.strftime('%Y-%m-%d %H:%M')},{self.preparacion},{self.duracion},{self.periodicidad.name}"