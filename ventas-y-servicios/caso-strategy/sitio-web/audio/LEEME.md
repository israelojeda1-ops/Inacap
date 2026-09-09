# Audios de la narración del recorrido

Estos seis archivos son la voz que se escucha en cada paso del recorrido
explicativo del juego, dentro de la ventana "Ver video explicativo".

| Archivo | Paso |
|---|---|
| `paso-1.mp3` | Qué es STRATEGY |
| `paso-2.mp3` | El tablero |
| `paso-3.mp3` | El turno y los dados |
| `paso-4.mp3` | Los mazos de cartas |
| `paso-5.mp3` | Una partida de ejemplo |
| `paso-6.mp3` | Cómo se gana |

No están grabados con un micrófono: se generaron con **es-CL-CatalinaNeural**,
la voz neuronal chilena de Microsoft, a través de `edge-tts`.

La ventaja de tenerlos como archivo es que **suenan igual en cualquier equipo**:
antes la narración dependía de las voces instaladas en el computador de quien
mirara, y en varios sonaba robótica.

## Cómo cambiarlos

Los textos no se escriben aquí: salen del propio `../index.html`, de la
propiedad `say` de cada paso. Si editas un texto ahí, vuelve a generar los
audios con:

```bash
python3 herramientas/generar-narracion.py                        # voz actual
python3 herramientas/generar-narracion.py es-CL-LorenzoNeural    # voz chilena masculina
python3 herramientas/generar-narracion.py es_AR-daniela-high     # con Piper, sin internet
```

El script avisa si algún audio quedó más largo que la duración de su paso, para
poder ajustarla en `../index.html`.

Las instrucciones completas (qué instalar, qué voces hay) están en la cabecera
de ese mismo script.

## Si prefieres tu propia voz

Puedes grabarte con el celular y reemplazar cualquiera de estos archivos
manteniendo el nombre. El sitio no distingue de dónde salió el audio.

Los comentarios de lo que va pasando —el dado, las respuestas de las cartas,
los turnos de la partida— no se pueden grabar, porque dependen de lo que haga
quien está mirando: esos los sigue diciendo la voz del navegador.
