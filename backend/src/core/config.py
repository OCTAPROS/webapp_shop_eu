import os
from dotenv import load_dotenv, find_dotenv

from pathlib import Path
# env_path = Path("..") / ".env"
# print(f"env_path: {env_path}")
# load_dotenv(dotenv_path=env_path)
load_dotenv(find_dotenv(".env"))


class Settings: 
    PROJECT_NAME : str = "Webbshopz"
    PROJECT_VERSION : str = "v1"
    
    ORACLE_DB_USERNAME: str = os.getenv("ORACLE_DB_USERNAME")
    ORACLE_DB_PASSWORD: str = os.getenv("ORACLE_DB_PASSWORD")
    ORACLE_DB_DSN: str = os.getenv("ORACLE_DB_DSN")
    ORACLE_DB_URL: str = f"oracle+oracledb://{ORACLE_DB_USERNAME}:{ORACLE_DB_PASSWORD}@{ORACLE_DB_DSN}"

    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY")
    JWT_ALGORITHM: str = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
settings = Settings()