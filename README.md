# 🚚 Proyecto Fundamentos de Programación — Entrega 1  
Este proyecto simula un sistema de logística entre almacenes, con envíos programados y transporte asociado. Está dividido en tres clases principales: `Almacen`, `Transporte` y `Envio`.

## 🧱 Estructura del proyecto  
src/  
└── entrega1/  
  ├── Almacen.py  
  ├── Transporte.py  
  ├── Envio.py  
  ├── Funciones.py  
  └── test/  
    ├── TestAlmacen.py  
    ├── TestTransporte.py  
    ├── TestEnvio.py  
    └── TestGestor.py  

## 🧪 Tests  
- Los tests unitarios están en `TestAlmacen.py`, `TestTransporte.py`, `TestEnvio.py`  
- El script `TestGestor.py` genera una salida por consola con ejemplos como los del PDF del entregable  
- Todos los envíos tienen transporte y fechas reales (no hay `None`)  

## 🚀 Cómo ejecutar  
Desde la raíz del proyecto:  
`python src/entrega1/test/TestGestor.py`  
Esto muestra ejemplos de creación de almacenes, transportes y envíos con datos simulados.

## 🧾 Notas personales  
- `Envio.envios()` genera una cadena de envíos entre almacenes consecutivos  
- `Transporte.random()` crea rutas aleatorias con periodicidad y duración  
- `siguiente_fecha_disponible()` calcula la próxima salida/llegada según la periodicidad  
- En el bucle de envíos, uso siempre `fecha_ref` para evitar `None` en `fecha_peticion`  
- El código está documentado y listo para entregar o reutilizar  

## 👨‍💻 Autor  
- Nombre: Manuel  
- UVUS: LXG7020  
- Fecha: Octubre 2025

---



