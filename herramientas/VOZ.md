# La voz de las narraciones

Esta es la ficha de la voz que usamos, para no tener que redescubrirla en cada
proyecto.

| | |
|---|---|
| **Voz** | `es-CL-CatalinaNeural` |
| **Quién la hace** | Microsoft (voz neuronal) |
| **Acento** | Chileno, femenino |
| **Cómo se llega a ella** | El paquete `edge-tts` de Python |
| **Alternativa chilena masculina** | `es-CL-LorenzoNeural` |
| **Alternativa sin internet** | `es_AR-daniela-high` con Piper (no hay voz chilena en Piper) |
| **Muestra** | `muestra-voz-catalina.mp3`, en esta misma carpeta |

## Generarla en un proyecto nuevo

```bash
pip install edge-tts
python3 -m edge_tts --voice es-CL-CatalinaNeural \
  --text "El texto que quieras escuchar." \
  --write-media salida.mp3
```

Necesita internet al momento de generar. El `.mp3` que queda después ya no
depende de nada.

## Para pedírselo a otra sesión de Claude

Copia y pega esto:

> Para las narraciones usa la voz `es-CL-CatalinaNeural` (voz neuronal chilena
> de Microsoft), generada con el paquete `edge-tts` de Python:
> `python3 -m edge_tts --voice es-CL-CatalinaNeural --text "..." --write-media salida.mp3`.
> Es la misma voz que usamos en el sitio de STRATEGY, en el repositorio
> israelojeda1-ops/Inacap. Ahí está el script `herramientas/generar-narracion.py`,
> que genera todas las narraciones de una vez y avisa si algún audio queda más
> largo que el espacio que tiene. Si la sesión no tiene internet, la alternativa
> es Piper con `es_AR-daniela-high`, pero esa es argentina: no existe voz
> chilena en Piper.

Si además quieres que escuche cómo suena, adjunta a esa conversación el archivo
`muestra-voz-catalina.mp3`.

## Un detalle que conviene saber

`edge-tts` usa el servicio de lectura en voz alta del navegador Edge. Es
gratuito y de uso habitual, pero sus términos apuntan a esa función del
navegador, así que para algo comercial conviene usar Azure Speech (la misma
voz, con licencia clara) o Piper, que es de código abierto sin condiciones.
