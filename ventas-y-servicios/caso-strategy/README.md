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
| `sitio-web/index.html` | La tienda online y el recorrido explicativo en un solo archivo (HTML, CSS y JS), 88 KB |
| `sitio-web/favicon.ico`, `favicon.svg`, `apple-touch-icon.png` | Ícono del sitio: un dado amarillo sobre azul |
| `sitio-web/audio/` | La narración de los seis pasos en `.mp3` (unas 540 KB en total) |
| `../../herramientas/generar-narracion.py` | Script que regenera esos audios con Piper |
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
  Mientras no haya un video grabado, la ventana reproduce un **recorrido
  interactivo** hecho en HTML, CSS y JavaScript, con seis pasos: qué es
  STRATEGY, el tablero, el turno con el dado, los cuatro mazos de cartas, una
  partida de ejemplo y cómo se gana. Avanza solo (1 minuto y 36 segundos en
  total) y trae barra de reproducción con pausa, paso anterior/siguiente,
  saltos por punto, botón de repetir y botón de sonido. Además se puede interactuar:
  tocar cualquier casilla del tablero para leer qué pasa al caer en ella,
  tirar el dado y ver avanzar la ficha, responder una carta de cada mazo
  (marca correcta o incorrecta y explica) y saltar a cualquier turno de la
  partida de ejemplo. El recorrido se detiene cuando alguien interactúa, para
  que pueda mirarlo con calma.
- El recorrido tiene **sonido**: una voz va describiendo lo que ocurre —el paso
  en el que va, la casilla que se toca, el número que sale en el dado, la carta
  elegida y si la respuesta estuvo bien o mal, y cada turno de la partida de
  ejemplo— más efectos de dado, avance de ficha, acierto y error.
- La narración de los seis pasos son **audios grabados** (`sitio-web/audio/`),
  hechos con la voz neuronal `es_AR-daniela-high` de Piper. Suenan igual en
  cualquier equipo. Se regeneran con `herramientas/generar-narracion.py`, que
  toma los textos del propio `index.html`; ver `sitio-web/audio/LEEME.md`.
  Piper no tiene voz chilena: se usó la argentina, la más cercana en acento.
- Los comentarios de lo que va pasando dependen de lo que haga quien mira, así
  que no se pueden grabar: los dice la voz del navegador (`speechSynthesis`).
  El sitio elige la mejor voz en español que tenga el equipo —ordenándolas por
  calidad y por acento más cercano a Chile— y deja un selector en la barra para
  cambiarla. En Windows conviene instalar la voz "Microsoft Catalina", que es
  chilena; el sitio la prefiere automáticamente si está.
- Los efectos de sonido se generan con `AudioContext`, sin archivos.
- Todo lo que se escucha aparece además escrito como subtítulo bajo la barra,
  así que se entiende igual con el sonido apagado o en un computador sin voces.
  El botón 🔊 de la barra silencia y reactiva, y la elección se recuerda en el
  navegador.
  Si más adelante se graba un video de verdad, basta con pegar el enlace en la
  constante `VIDEO_URL` al inicio del script del `index.html` (acepta enlaces
  normales de YouTube o Vimeo) y la ventana pasa a mostrar ese video en lugar
  del recorrido.
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
- [ ] El video explicativo está resuelto con el recorrido interactivo del
      sitio, no con un video grabado. Si la profesora pide un video real,
      hay que grabarlo y pegar el enlace en `VIDEO_URL`.
- [ ] Los ejercicios y la partida de ejemplo del recorrido son contenido de
      muestra (7 × 8, múltiplos de 6, dos jugadores llamados María y Diego).
      Se pueden cambiar en el arreglo `DECKS` y en `PLAY` dentro del script.
- [ ] El correo, el WhatsApp y el Instagram del pie de página son ficticios.
- [ ] El pago está simulado: el sitio no procesa transacciones reales y así lo
      declara en pantalla. Si alguna vez se quisiera cobrar de verdad haría falta
      integrar Webpay o Mercado Pago, lo que requiere un servidor.
- [ ] Subir el informe `.docx` a `informe/`.
- [ ] Confirmar estado de la entrega y fecha de entrega.
