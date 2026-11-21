# Asistente de Registro de Actividades

Proyecto Flask refactorizado para separar interfaz, reglas del agente, skills y persistencia JSON. El agente es local y determinista: el proyecto original no incluía integración LLM ni requiere API o credenciales.

## Arquitectura

```text
app.py                         Rutas Flask y coordinación
agent/activity_agent.py        Agente y ciclo de hasta 3 iteraciones
agent/agent_config.py           Rol y valores predeterminados del agente
agent/AGENT_PROFILE.md          Perfil, política de decisión y estilo de salida
agent/skills/                   Capacidades reutilizables
  activity_completion/SKILL.md  Instrucciones de normalización y completado
  activity_validation/SKILL.md  Reglas de validación
activity_store.py               Persistencia JSON segura/atómica
registro.py                     Catálogo de categorías y compatibilidad
actividades.json                 Datos de la aplicación
```

## Flujo del agente

1. La ruta recibe el borrador del formulario.
2. `ActivityAgent` ejecuta las skills de completado y validación hasta tres iteraciones, o hasta que no haya cambios (convergencia).
3. La skill deriva categoría válida, color del catálogo y comentario si faltan; la duración y fecha cuentan con valores predeterminados.
4. El validador verifica campos y fecha calendario. Si algo esencial no se puede inferir, devuelve un mensaje claro en lugar de solicitar una conversación manual.
5. `ActivityStore` guarda la ficha con reemplazo atómico del archivo JSON.

El título es el único campo indispensable que debe aportar quien registra, porque inventarlo podría crear un evento falso. El resto de campos opcionales se completa automáticamente. El ciclo es reproducible y auditable; no se presenta como un LLM, ya que el proyecto base no tenía proveedor ni flujo LLM.

## Refactorización: antes y después

```python
"""
ANTES — ruta acoplada a formulario, catálogo y archivo:
    categoria = request.form["categoria"]
    color = colores[categoria]
    guardar_en_json("actividades.json", {
        "categoria": categoria,
        "descripcion": request.form["descripcion"],
        "color": color,
    })

DESPUÉS — composición modular realmente usada por la aplicación:
    borrador = request.form.to_dict()
    actividad = agent.prepare(borrador)  # skills iterativas: completar + validar
    store.append(actividad)              # persistencia atómica separada
"""
```

El bloque “después” corresponde a la ruta `/publicar` de `app.py`; no es pseudocódigo aislado. Las reglas están en `agent/skills/` y el acceso JSON en `activity_store.py`.

## Ejecución

Requiere Python 3.10+ y Flask:

```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Abrir http://127.0.0.1:5000. Para una instalación ligera, `requirements.txt` solo necesita Flask:

```text
Flask>=3.1,<4
```

## Datos

`actividades.json` contiene una lista de objetos con `categoria`, `descripcion`, `duracion`, `comentario`, `fecha` y `color`. Las fechas nuevas se normalizan como `YYYY/MM/DD`. El almacén inicializa una lista vacía si el archivo falta o está vacío y rechaza estructuras JSON con forma incorrecta.

## Uso de IA y criterio de diseño

La asistencia de IA se usó para proponer estructura y detección de acoplamientos. Se mantuvo criterio humano al evitar incorporar un servicio LLM sin existir en el proyecto, mantener deterministas las reglas de negocio, no inventar títulos y aislar explícitamente las capacidades en skills revisables. La lógica de completado y validación puede ejecutarse y auditarse sin conexión externa.
