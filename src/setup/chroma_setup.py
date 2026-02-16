"""
ChromaDB setup module.

This module initializes and verifies the ChromaDB persistent client.
"""
import logging
from typing import List

import chromadb
from chromadb.config import Settings
from chromadb.api.models.Collection import Collection

from src.config import get_config


# Configure logging
config = get_config()
logging.basicConfig(
    level=getattr(logging, config.get_log_level()),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def setup_chroma_client() -> chromadb.PersistentClient:
    """
    Initialize and return a ChromaDB persistent client.
    
    Returns:
        chromadb.PersistentClient: Initialized ChromaDB client
        
    Raises:
        Exception: If client initialization fails
    """
    try:
        config_instance = get_config()
        client = chromadb.PersistentClient(
            path=config_instance.get_chroma_path(),
            settings=Settings(
                anonymized_telemetry=config_instance.get_telemetry_setting()
            )
        )
        logger.info(
            f"ChromaDB client initialized at path: {config_instance.get_chroma_path()}"
        )
        return client
    except Exception as e:
        logger.error(f"Failed to initialize ChromaDB client: {e}")
        raise


def list_collections(client: chromadb.PersistentClient) -> List[Collection]:
    """
    List all collections in the ChromaDB client.
    
    Args:
        client: ChromaDB client instance
        
    Returns:
        List[Collection]: List of collection objects
        
    Raises:
        Exception: If listing collections fails
    """
    try:
        collections = client.list_collections()
        logger.info(f"Found {len(collections)} collection(s)")
        return collections
    except Exception as e:
        logger.error(f"Failed to list collections: {e}")
        raise


if __name__ == "__main__":
    try:
        client = setup_chroma_client()
        collections = list_collections(client)
        logger.info(f"Collections: {[col.name for col in collections]}")
    except Exception as e:
        logger.error(f"Setup failed: {e}")
        exit(1)
