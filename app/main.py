from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import marca_route
from app.database import Base, engine

# Crear tablas
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Gestión de Marcas")

# Configuración de CORS agregar los orígenes permitidos
origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(marca_route.router)
