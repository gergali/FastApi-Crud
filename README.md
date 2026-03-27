# FastAPI CRUD - Productos y Categorías

Proyecto de práctica backend con FastAPI, SQLAlchemy y Pydantic.  
Implementa un CRUD para productos y categorías, con validaciones básicas y manejo de errores.

## Funcionalidades
- Crear, listar, actualizar y eliminar productos.
- Crear, listar, actualizar y eliminar categorías.
- Validaciones con Pydantic (ejemplo: stock > 0).
- Manejo de errores con HTTPException.
- Documentación automática en `/docs` (Swagger UI).

## Estructura del proyecto
- `main.py` → configuración de FastAPI y endpoints.
- `crud.py` → lógica de acceso a datos.
- `models.py` → modelos SQLAlchemy.
- `schemas.py` → schemas Pydantic.
- `requirements.txt` → dependencias.

## Instalación y ejecución
Clonar el repositorio y levantar el servidor:

```bash
git clone https://github.com/gergali/fastapi-crud.git
cd fastapi-crud
pip install -r requirements.txt
uvicorn main:app --reload

El servidor se inicia en http://127.0.0.1:8000  
La documentación interactiva está en http://127.0.0.1:8000/docs.

-----------------Ejemplos de uso------------
##  Crear categoría
json
POST /categorias
{
  "nombre": "Electrónica"
}
## Crear producto
json
POST /productos
{
  "nombre": "Mouse Gamer",
  "stock": 50,
  "categoria_id": 1
}
##Conocimientos aplicados
FastAPI para construcción de APIs REST.

SQLAlchemy para persistencia en base de datos.

Pydantic para validación de datos.

Buenas prácticas de modularidad y manejo de errores.
