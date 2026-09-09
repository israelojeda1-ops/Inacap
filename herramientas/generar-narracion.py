#!/usr/bin/env python3
"""Genera la narración del recorrido explicativo con una voz neuronal (Piper).

Los archivos que produce quedan en ventas-y-servicios/caso-strategy/sitio-web/audio/
y son los que reproduce el sitio en cada paso.

Preparación (una sola vez):

    pip install piper-tts imageio-ffmpeg
    mkdir -p .voces && cd .voces
    python3 -m piper.download_voices es_AR-daniela-high

Uso:

    python3 herramientas/generar-narracion.py                  # voz por defecto
    python3 herramientas/generar-narracion.py es_AR-daniela-high

Voces en español disponibles (se listan con `python3 -m piper.download_voices`):

    es_AR-daniela-high     Argentina, la que usa hoy el sitio
    es_MX-claude-high      México
    es_ES-sharvard-medium  España
    es_ES-davefx-medium    España
    es_MX-ald-medium       México, más liviana

No hay voz chilena: Piper no publica una es-CL, así que se eligió la más
cercana en acento entre las que sí existen.

Los modelos NO se guardan en el repositorio: pesan entre 60 y 115 MB cada uno.
Por eso la carpeta .voces/ está en el .gitignore.

Los textos no se escriben aquí: se leen del propio index.html, para que el
audio y el subtítulo nunca queden diciendo cosas distintas.
"""
import io, json, os, re, subprocess, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITIO = os.path.join(RAIZ, "ventas-y-servicios", "caso-strategy", "sitio-web")
VOCES = os.environ.get("PIPER_VOCES", os.path.join(RAIZ, ".voces"))
VOZ = sys.argv[1] if len(sys.argv) > 1 else "es_AR-daniela-high"
MODELO = os.path.join(VOCES, VOZ + ".onnx")
DESTINO = os.path.join(SITIO, "audio")

import imageio_ffmpeg
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()

# los textos se leen del propio index.html, para que audio y subtítulo no se separen
html = io.open(os.path.join(SITIO, "index.html"), encoding="utf-8").read()
textos = re.findall(r'say:"((?:[^"\\]|\\.)*)"', html)
assert len(textos) == 6, "se esperaban 6 pasos, hay %d" % len(textos)

# los símbolos se dicen como palabras, igual que en el sitio
def en_palabras(t):
    t = t.replace("×", " por ").replace("÷", " dividido en ")
    t = re.sub(r"\s*=\s*\?", ", ¿cuánto es?", t)
    t = re.sub(r"\s*=\s*", " es igual a ", t)
    t = re.sub(r"(\d)\s*[−–-]\s*(\d)", r"\1 menos \2", t)
    for n, p in [("4°","cuarto"),("5°","quinto"),("6°","sexto"),("7°","séptimo"),("8°","octavo")]:
        t = t.replace(n, p)
    return re.sub(r"\s{2,}", " ", t).strip()

os.makedirs(DESTINO, exist_ok=True)
for i, txt in enumerate(textos, 1):
    wav = os.path.join(DESTINO, "_tmp-paso-%d.wav" % i)
    mp3 = os.path.join(DESTINO, "paso-%d.mp3" % i)
    subprocess.run(["python3", "-m", "piper", "-m", MODELO, "-f", wav],
                   input=en_palabras(txt), text=True, check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-i", wav,
                    "-codec:a", "libmp3lame", "-b:a", "64k", "-ar", "22050", "-ac", "1", mp3], check=True)
    dur = subprocess.run([FFMPEG, "-i", mp3], capture_output=True, text=True).stderr
    d = re.search(r"Duration: (\d+):(\d+):([\d.]+)", dur)
    seg = int(d.group(2)) * 60 + float(d.group(3)) if d else 0
    print("paso %d  %5.1f s  %6.1f KB  %s" % (i, seg, os.path.getsize(mp3)/1024, os.path.basename(mp3)))
    os.remove(wav)
print("voz usada:", VOZ)
