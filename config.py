import os

class Settings:
    PROJECT_NAME: str = "API de Cursos de Tecnologia Online"
    VERSION: str = "1.0.0"
    HOST: str = os.getenv("HOST", "127.0.0.1")  # Pode ser definido como variável de ambiente
    PORT: int = int(os.getenv("PORT", 8000))  # Pode ser definido como variável de ambiente
    ALLOW_ORIGINS: list[str] = ["*"]  # Ajuste conforme necessário

settings = Settings()