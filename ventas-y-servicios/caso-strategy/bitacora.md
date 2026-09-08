# Bitácora · Caso STRATEGY

Entradas en orden cronológico inverso (la más reciente arriba).

## 2026-09-08 — Se incorpora el prototipo original de la tienda y se separan sus imágenes

- Se reemplaza la versión reconstruida por el `index.html` original del
  grupo. Las cinco imágenes en base64 (tres distintas) pasan a
  `sitio-web/img/`; el HTML baja de 642 KB a 47 KB.
- Probado en local con `python3 -m http.server` y Chromium (escritorio y
  celular): botón "Ver qué incluye", enlaces del menú, agregar y quitar del
  carrito, cupón `APRENDE15`, cambio de despacho, formulario de pago con RUT
  válido e inválido, cotización y preguntas frecuentes. Todo funciona.
- Único detalle: no hay favicon (404 inofensivo).

## 2026-09-08 — Se reconstruye la tienda online completa

- Se reemplaza la página provisoria por el sitio completo en `sitio-web/index.html`
  (un solo archivo HTML con CSS y JS): hero, beneficios, cómo se juega con el botón
  "Ver qué incluye", tipos de cartas, tienda con carrito, cupón `APRENDE15`,
  cálculo de despacho, pago simulado con validación de RUT, cotización para
  colegios y contacto.
- Las imágenes van como archivos separados en `sitio-web/img/` (optimizadas a
  menos de 300 KB cada una) en lugar de base64.
- Probado en local con Chromium en escritorio y móvil: 43 comprobaciones
  automáticas sin errores de consola.

## 2026-09-08 — Se agregan el afiche y la imagen de producto

- Se suben `material/afiche-strategy.jpg` y `material/producto-strategy.jpg`.
- La imagen de producto se muestra también en la página provisoria del sitio
  (`sitio-web/img/producto-strategy.jpg`).

## 2026-09-08 — Publicación en Vercel

- Se crea el proyecto `strategy-inacap` en Vercel enlazado al repositorio, con
  directorio raíz `sitio-web/`. URL pública: https://strategy-inacap.vercel.app
- Se sube un `index.html` provisorio de "sitio en construcción" que será
  reemplazado por la tienda real cuando llegue el archivo.

## 2026-09-08 — Creación del proyecto en el repositorio

- Se crea la carpeta `ventas-y-servicios/caso-strategy/` con `informe/`,
  `sitio-web/img/`, `material/`, README y bitácora.
- Quedan anotados los pendientes conocidos: precios de ejemplo, datos de
  contacto ficticios y pago simulado.
- Aún no se han subido el informe, el `index.html` ni las imágenes. La
  separación de las imágenes en base64 a `sitio-web/img/` queda pendiente
  hasta contar con el archivo.
