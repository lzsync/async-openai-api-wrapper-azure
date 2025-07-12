from pydantic import (Field)
from pydantic_settings import BaseSettings

class Config(BaseSettings, frozen=True):
    LLM_DEPLOYMENT_NAME: str
    EMBEDDING_DEPLOYMENT_NAME: str
    DEFAULT_CRED: str
    API_VERSION: str
    ENDPOINT: str
    MAX_RETRIES: int = Field(strict=False, ge=0)
    TIMEOUT_SECONDS: int = Field(strict=False, gt=0)