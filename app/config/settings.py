from dataclasses import dataclass
import os

from dotenv import load_dotenv


@dataclass
class Settings:
    DATABASE: str
    USUERNAME: str
    PASSWORD: str
    BD_PORT: str
    HOST: str


load_dotenv()

settings: Settings = Settings(
    DATABASE=os.getenv("DATABASE"),
    USUERNAME=os.getenv("USUERNAME"),
    PASSWORD=os.getenv("PASSWORD"),
    BD_PORT=os.getenv("BD_PORT"),
    HOST=os.getenv("HOST"),
)
