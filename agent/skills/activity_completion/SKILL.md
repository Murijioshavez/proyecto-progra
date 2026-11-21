# Skill: completar actividad

## Propósito
Normalizar una ficha de actividad y derivar datos seguros (categoría canónica,
color y comentario breve) cuando el formulario los omite.

## Instrucciones
1. Recibir un diccionario de actividad.
2. Recortar espacios y normalizar el nombre de categoría sin distinguir mayúsculas.
3. Si la categoría no existe, asignar «Actividades recreativas».
4. Derivar el color exclusivamente del catálogo; nunca aceptar un color arbitrario.
5. Si falta duración, usar «Por definir»; si falta comentario, describir brevemente la categoría y el título.
6. No inventar título. No pedir intervención al usuario: devolver el resultado para que el validador lo revise.

## Salida
Un diccionario con `categoria`, `color`, `descripcion`, `duracion`, `comentario` y `fecha`.
