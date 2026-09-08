# Caso STRATEGY · proceso de ventas y creación de valor

- **Asignatura:** Ventas y Servicios
- **Docente:** Patricia Angélica Rubilar Salinas
- **Integrantes:** Sofía Valenzuela, Román Aros y María Morales
- **Estado:** PENDIENTE
- **Fecha de entrega:** PENDIENTE

## Descripción

Análisis del proceso de ventas y de la creación de valor de STRATEGY, un juego
de mesa educativo para aprender matemáticas de 4° a 8° básico. El informe cubre
la evolución de las ventas, el ciclo de venta (preventa, venta y postventa), el
comportamiento del consumidor, los tipos de venta y el método AIDA.

Como complemento hay un sitio web de venta online en un solo archivo HTML, con
carrito funcional, códigos de descuento, cálculo de despacho, formulario de
compra con validación de RUT chileno y un formulario aparte de cotización para
colegios y fundaciones.

## Archivos

| Ruta | Contenido |
|---|---|
| `informe/` | El informe en `.docx` (aún no subido) |
| `sitio-web/` | La tienda online: `index.html` más las imágenes en `sitio-web/img/` (aún no subidos) |
| `material/` | Afiches e imágenes de producto (aún no subidos) |
| `bitacora.md` | Historial de cambios del proyecto |

## Cómo ver el sitio web en local

```bash
cd ventas-y-servicios/caso-strategy/sitio-web
python3 -m http.server 8000
# abrir http://localhost:8000
```

## Pendientes

- [ ] Los precios del sitio ($24.990 el juego y $109.990 el Pack Aula) son de
      ejemplo y hay que confirmarlos.
- [ ] El correo, el WhatsApp y el Instagram del pie de página son ficticios.
- [ ] El pago está simulado: el sitio no procesa transacciones reales y así lo
      declara en pantalla. Si alguna vez se quisiera cobrar de verdad haría falta
      integrar Webpay o Mercado Pago, lo que requiere un servidor.
- [ ] Subir el informe, el `index.html` y el material a sus carpetas.
- [ ] Separar las imágenes en base64 del `index.html` a archivos en `sitio-web/img/`.
- [ ] Confirmar estado de la entrega y fecha de entrega.
