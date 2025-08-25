# Gestión de Marcas - FastAPI

Esta es una aplicación backend desarrollada con **FastAPI** para gestionar marcas. Permite crear, actualizar y listar marcas usando un API REST, con persistencia en base de datos mediante **SQLAlchemy**.

---

## Tecnologías

- Python 3.11+
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn
- Base de datos: PostgreSQL (o MySQL/SQLite según configuración)
- Dependencias gestionadas con `requirements.txt`

---

## Instalación

1. Clonar el repositorio:

```bash
git clone <URL_DEL_REPOSITORIO>
cd gestion-marcas-back


2. Crear un entorno virtual:

python -m venv venv
source venv/bin/activate # Linux/Mac
venv\Scripts\activate    # Windows

3. Instalar dependencias

pip install -r requirements.txt

4. Ejecución

uvicorn app.main:app --reload