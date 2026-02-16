"""
Central configuration management for ChromaDB.

This module provides centralized configuration using environment variables
with sensible defaults. Supports loading from .env files using python-dotenv.
"""
import os
from typing import Optional

# Try to load .env file if python-dotenv is available
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    # python-dotenv is optional
    pass


class Config:
    """Configuration class for ChromaDB settings."""
    
    # ChromaDB Settings
    CHROMA_PATH: str = os.getenv("CHROMA_PATH", "./chroma")
    CHROMA_COLLECTION: str = os.getenv("CHROMA_COLLECTION", "sample")
    
    # Telemetry Settings
    ANONYMIZED_TELEMETRY: bool = os.getenv(
        "ANONYMIZED_TELEMETRY", "False"
    ).lower() in ("true", "1", "yes")
    
    # Logging Settings
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    
    @classmethod
    def get_chroma_path(cls) -> str:
        """Get the ChromaDB persistence path."""
        return cls.CHROMA_PATH
    
    @classmethod
    def get_collection_name(cls) -> str:
        """Get the default collection name."""
        return cls.CHROMA_COLLECTION
    
    @classmethod
    def get_telemetry_setting(cls) -> bool:
        """Get the telemetry setting."""
        return cls.ANONYMIZED_TELEMETRY
    
    @classmethod
    def get_log_level(cls) -> str:
        """Get the logging level."""
        return cls.LOG_LEVEL


def get_config() -> Config:
    """
    Get the application configuration.
    
    Returns:
        Config: Configuration instance
    """
    return Config()
