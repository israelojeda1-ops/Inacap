#!/usr/bin/env python3
"""Genera la narración del recorrido explicativo del sitio de STRATEGY.

Los archivos que produce quedan en ventas-y-servicios/caso-strategy/sitio-web/audio/
y son los que se escuchan en cada paso del recorrido.

Los textos NO se escriben aquí: se leen del propio index.html, de la propiedad
`say` de cada paso, para que el audio y el subtítulo nunca queden diciendo
cosas distintas.

--------------------------------------------------------------------------
Dos motores de voz, según el nombre que se pida
--------------------------------------------------------------------------

1. Voces de Microsoft (nombres con guión: es-CL-CatalinaNeural)
   Son las únicas con acento chileno. Se usan a través de edge-tts, que es
   gratuito pero necesita internet al momento de generar (los .mp3 que quedan
   después no dependen de nada).

       pip install edge-tts
       python3 -m edge_tts --list-voices | grep es-

   Voces en español que interesan:

       es-CL-CatalinaNeural   Chile, mujer   <- la que usa hoy el sitio
       es-CL-LorenzoNeural    Chile, hombre
       es-MX-DaliaNeural      México, mujer
       es-AR-ElenaNeural      Argentina, mujer

2. Voces de Piper (nombres con guión bajo: es_AR-daniela-high)
   Motor de código abierto, funciona sin internet. No tiene voz chilena.

       pip install piper-tts
       mkdir -p .voces && cd .voces
       python3 -m piper.download_voices es_AR-daniela-high

   Voces disponibles: es_AR-daniela-high, es_MX-claude-high,
   es_ES-sharvard-medium, es_ES-davefx-medium, es_MX-ald-medium.
   Los modelos pesan entre 60 y 115 MB, por eso .voces/ está en el .gitignore.

En los dos casos hace falta ffmpeg para dejar los audios en mp3:

       pip install imageio-ffmpeg

--------------------------------------------------------------------------
Uso
--------------------------------------------------------------------------

    python3 herramientas/generar-narracion.py                       # voz actual
    python3 herramientas/generar-narracion.py es-CL-LorenzoNeural   # otra voz
    python3 herramientas/generar-narracion.py es_AR-daniela-high    # con Piper

Después de generar, revisa que cada audio quepa en la duración de su paso: el
script imprime cuánto dura cada uno y cuánto dura el paso en el sitio, y avisa
si alguno se pasa. La duración de los pasos se ajusta en `dur`, dentro del
mismo index.html.

Nota: si trabajas detrás de un proxy con certificado propio, edge-tts puede
fallar con "certificate verify failed". En ese caso hay que agregar el
certificado del proxy al archivo de certifi (python3 -c "import certifi;
print(certifi.where())").
"""

import io
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITIO = os.path.join(RAIZ, "ventas-y-servicios", "caso-strategy", "sitio-web")
VOCES = os.environ.get("PIPER_VOCES", os.path.join(RAIZ, ".voces"))
DESTINO = os.path.join(SITIO, "audio")
VOZ = sys.argv[1] if len(sys.argv) > 1 else "es-CL-CatalinaNeural"

import imageio_ffmpeg
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()

html = io.open(os.path.join(SITIO, "index.html"), encoding="utf-8").read()
textos = re.findall(r'say:"((?:[^"\\]|\\.)*)"', html)
pasos = [int(d) / 1000.0 for d in re.findall(r"dur:(\d+)", html)]
assert len(textos) == 6, "se esperaban 6 pasos, hay %d" % len(textos)


def en_palabras(t):
    """Los símbolos se dicen como palabras, igual que en el sitio."""
    t = t.replace("×", " por ").replace("÷", " dividido en ")
    t = re.sub(r"\s*=\s*\?", ", ¿cuánto es?", t)
    t = re.sub(r"\s*=\s*", " es igual a ", t)
    t = re.sub(r"(\d)\s*[−–-]\s*(\d)", r"\1 menos \2", t)
    for n, p in [("4°", "cuarto"), ("5°", "quinto"), ("6°", "sexto"),
                 ("7°", "séptimo"), ("8°", "octavo")]:
        t = t.replace(n, p)
    return re.sub(r"\s{2,}", " ", t).strip()


def con_edge(texto, salida):
    subprocess.run([sys.executable, "-m", "edge_tts", "--voice", VOZ,
                    "--text", texto, "--write-media", salida],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)


def con_piper(texto, salida):
    modelo = os.path.join(VOCES, VOZ + ".onnx")
    if not os.path.exists(modelo):
        sys.exit("Falta el modelo %s.\nDescárgalo con:\n"
                 "  mkdir -p %s && cd %s && python3 -m piper.download_voices %s"
                 % (modelo, VOCES, VOCES, VOZ))
    wav = salida + ".wav"
    subprocess.run([sys.executable, "-m", "piper", "-m", modelo, "-f", wav],
                   input=texto, text=True, check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-i", wav,
                    "-codec:a", "libmp3lame", "-b:a", "64k", "-ar", "22050",
                    "-ac", "1", salida], check=True)
    os.remove(wav)


def duracion(mp3):
    salida = subprocess.run([FFMPEG, "-i", mp3], capture_output=True, text=True).stderr
    m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", salida)
    return int(m.group(2)) * 60 + float(m.group(3)) if m else 0.0


microsoft = "-" in VOZ and "_" not in VOZ
os.makedirs(DESTINO, exist_ok=True)
apretados = []

for i, texto in enumerate(textos, 1):
    mp3 = os.path.join(DESTINO, "paso-%d.mp3" % i)
    (con_edge if microsoft else con_piper)(en_palabras(texto), mp3)
    dur, paso = duracion(mp3), pasos[i - 1] if i <= len(pasos) else 0
    holgura = paso - dur
    if holgura < 0.5:
        apretados.append((i, dur, paso))
    print("paso %d  voz %5.1f s   paso %5.1f s   %6.1f KB%s"
          % (i, dur, paso, os.path.getsize(mp3) / 1024,
             "   <-- el paso queda corto" if holgura < 0.5 else ""))

print("voz usada: %s (%s)" % (VOZ, "Microsoft" if microsoft else "Piper"))
if apretados:
    print("\nAjusta `dur` en index.html para estos pasos, dejando al menos "
          "medio segundo de aire después de la voz:")
    for i, dur, paso in apretados:
        print("  paso %d: la voz dura %.1f s y el paso %.1f s" % (i, dur, paso))
