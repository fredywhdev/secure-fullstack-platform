import os

class Settings:
    PROJECT_NAME = "Secure FullStack Platform"
    SECRET_KEY = os.getenv("SECRET_KEY", "change_me")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("JWT_EXPIRE_MINUTES", 30))
    DATABASES_URL = os.getenv("DATABASE_URL")

settings = Settings()