from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List
import itertools
from src.entrega1.Transporte import Transporte

# Generador automático de códigos únicos para cada envío
_codigo_envio = itertools.count(1)

@dataclass(frozen=True)
class Envio:
    """
    Clase que representa un envío de productos entre dos almacenes.
    Es inmutable y contiene toda la información necesaria para identificar el envío.
    """
    codigo: int = field(default_factory=lambda: next(_codigo_envio))  # Identificador único autogenerado
    fecha_peticion: Optional[datetime] = None  # Fecha en que se solicita el envío
    al1: int = 0  # Identificador del almacén de origen
    al2: int = 0  # Identificador del almacén de destino
    transporte: Optional[Transporte] = None  # Transporte asociado al envío
    fecha_de_salida: Optional[datetime] = None  # Fecha de salida del envío
    fecha_de_llegada: Optional[datetime] = None  # Fecha de llegada del envío

    @staticmethod
    def of(fecha_peticion: datetime, al1: int, al2: int,
           transporte: Optional[Transporte] = None,
           salida: Optional[datetime] = None,
           llegada: Optional[datetime] = None) -> Envio:
        """
        Método de factoría para crear un objeto Envio con los datos básicos.
        Permite incluir transporte y fechas si están disponibles.
        """
        return Envio(fecha_peticion=fecha_peticion, al1=al1, al2=al2,
                     transporte=transporte, fecha_de_salida=salida, fecha_de_llegada=llegada)

    @staticmethod
    def envios(fecha: datetime, almacenes: List[int]) -> List[Envio]:
        """
        Genera una lista de envíos conectando cada almacén con el siguiente.
        El primer envío incluye la fecha de petición; los demás no.
        """
        lista = []
        for i in range(len(almacenes) - 1):
            peticion = fecha if i == 0 else None
            envio = Envio.of(peticion, almacenes[i], almacenes[i + 1])
            lista.append(envio)
        return lista

    def __str__(self) -> str:
        """
        Representación en cadena del envío, útil para imprimir en consola.
        """
        return (f"Envio {self.codigo}: al1={self.al1}, al2={self.al2}, "
                f"fecha_peticion={self.fecha_peticion}, salida={self.fecha_de_salida}, "
                f"llegada={self.fecha_de_llegada}")