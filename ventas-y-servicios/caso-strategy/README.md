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
| `sitio-web/index.html` | La tienda online en un solo archivo (HTML, CSS y JS), 47 KB |
| `sitio-web/img/` | Las tres imágenes del sitio (`hero-juego.jpg`, `tablero.jpg`, `cartas.jpg`), antes incrustadas en base64 |
| `material/afiche-strategy.jpg` | Afiche publicitario del juego (1024×1536) |
| `material/producto-strategy.jpg` | Imagen de producto: caja, tablero, cartas y fichas (1536×1024) |
| `bitacora.md` | Historial de cambios del proyecto |

## Sitio publicado

- **URL pública:** https://strategy-inacap.vercel.app
- **Proyecto Vercel:** `strategy-inacap` (team `israelojeda1-ops-projects`), con
  directorio raíz `ventas-y-servicios/caso-strategy/sitio-web`.
- Cada push a la rama de producción del repo publica automáticamente.

## Funciones del sitio web

- Catálogo con el juego ($24.990), el Pack Aula ($109.990) y compra
  institucional por cotización.
- Carrito lateral con cantidades y eliminación de productos.
- Códigos de descuento `APRENDE15` (15%) y `PROFE10` (10%).
- Despacho: $3.990 a domicilio, gratis sobre $50.000 o con retiro en punto
  de entrega.
- Formulario de pago con validación de RUT chileno (módulo 11), correo,
  teléfono, región y dirección. El pago es simulado y así se declara en
  pantalla.
- Formulario aparte de cotización para colegios y fundaciones.
- Ventana de video explicativo (botón "Ver video explicativo" en la portada).
  El enlace se configura en la constante `VIDEO_URL` al inicio del script del
  `index.html`; acepta enlaces normales de YouTube o Vimeo. Mientras esté
  vacío muestra un aviso de "próximamente".
- Preguntas frecuentes en acordeón y diseño responsive (en celular el menú
  superior se oculta y queda visible el botón del carrito).

## Cómo ver el sitio web en local

```bash
cd ventas-y-servicios/caso-strategy/sitio-web
python3 -m http.server 8000
# abrir http://localhost:8000
```

## Pendientes

- [ ] Los precios del sitio ($24.990 el juego y $109.990 el Pack Aula) son de
      ejemplo y hay que confirmarlos.
- [ ] El sitio no tiene favicon; el navegador pide `/favicon.ico` y recibe 404.
- [ ] Falta el enlace del video explicativo (`VIDEO_URL` en `index.html`).
- [ ] El correo, el WhatsApp y el Instagram del pie de página son ficticios.
- [ ] El pago está simulado: el sitio no procesa transacciones reales y así lo
      declara en pantalla. Si alguna vez se quisiera cobrar de verdad haría falta
      integrar Webpay o Mercado Pago, lo que requiere un servidor.
- [ ] Subir el informe `.docx` a `informe/`.
- [ ] Confirmar estado de la entrega y fecha de entrega.
