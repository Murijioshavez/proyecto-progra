# Skill: validar actividad

## Propósito
Aplicar reglas locales antes de persistir una ficha.

## Instrucciones
- Confirmar que la categoría pertenezca al catálogo.
- Exigir un título no vacío.
- Confirmar duración presente.
- Aceptar fechas calendario válidas en formato `YYYY/MM/DD`.
- Devolver una lista de errores; no solicitar aclaraciones humanas.

El orquestador vuelve a ejecutar las skills hasta el límite configurado y luego
entrega un error legible si un dato esencial no se puede inferir con seguridad.
