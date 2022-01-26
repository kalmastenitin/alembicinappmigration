from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    db_username: str = Field('test', env='DB_USERNAME')
    db_secret: str = Field('test', env='DB_SECRET')
    db_host: str = Field('test', env='DB_HOST')
    db_port: int = Field(3306, env='DB_PORT')
    db_name: str = Field('test', env='DB_NAME')

    class Config:
        env_file = ".env"


def create_app():
    app = FastAPI(
        title="Fastapi Automigration With Alembic/SqlAlchemy",
        description="Run alembic migrations from inside fastapi application, it is useful for redistributable applications.",
        version="1.0.0",
        docs_url="/api/docs"

    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    from .routes import router as service_router
    app.include_router(service_router, prefix="/api")
    return app


app = create_app()
