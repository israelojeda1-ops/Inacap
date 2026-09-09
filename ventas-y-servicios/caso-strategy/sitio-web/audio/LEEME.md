# Audios del recorrido explicativo (opcional)

Esta carpeta está vacía a propósito.

La narración del recorrido la hace hoy la voz del navegador. Si prefieres una
voz humana —por ejemplo grabándote tú misma con el celular—, graba un audio por
paso, déjalos aquí y nómbralos en el archivo `../index.html`, en la línea:

```js
var VOZ_GRABADA = ["", "", "", "", "", ""];
```

Por ejemplo:

```js
var VOZ_GRABADA = ["audio/paso-1.mp3", "audio/paso-2.mp3", "audio/paso-3.mp3",
                   "audio/paso-4.mp3", "audio/paso-5.mp3", "audio/paso-6.mp3"];
```

Los seis pasos, en orden, son:

1. Qué es STRATEGY
2. El tablero
3. El turno y los dados
4. Los mazos de cartas
5. Una partida de ejemplo
6. Cómo se gana

No hace falta grabarlos todos: el paso que tenga archivo se escucha grabado y
los demás siguen con la voz del navegador. Los comentarios de lo que va
pasando (el dado, las respuestas, los turnos) siempre los dice el navegador,
porque dependen de lo que haga quien está mirando.

Formato recomendado: `.mp3`, voz clara, sin música de fondo. Si el audio dura
más que el paso, conviene alargar ese paso en la constante `dur` del mismo
script.
