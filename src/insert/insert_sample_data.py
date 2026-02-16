"""
Module for inserting sample data into ChromaDB.

This module provides functionality to insert sample documents
into the ChromaDB collection for testing and demonstration purposes.
"""
import logging
from typing import List, Dict, Any, Optional

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


def get_chroma_client() -> chromadb.PersistentClient:
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
        logger.info("ChromaDB client initialized")
        return client
    except Exception as e:
        logger.error(f"Failed to initialize ChromaDB client: {e}")
        raise


def get_or_create_collection(
    client: chromadb.PersistentClient,
    collection_name: Optional[str] = None
) -> Collection:
    """
    Get or create a collection in ChromaDB.
    
    Args:
        client: ChromaDB client instance
        collection_name: Name of the collection (uses config default if None)
        
    Returns:
        Collection: ChromaDB collection object
        
    Raises:
        Exception: If collection retrieval/creation fails
    """
    try:
        if collection_name is None:
            collection_name = get_config().get_collection_name()
            
        collection = client.get_or_create_collection(collection_name)
        logger.info(f"Using collection: {collection_name}")
        return collection
    except Exception as e:
        logger.error(f"Failed to get/create collection: {e}")
        raise


def insert_sample_data(
    collection: Collection,
    ids: List[str],
    documents: List[str],
    metadatas: Optional[List[Dict[str, Any]]] = None
) -> None:
    """
    Insert sample data into a ChromaDB collection.
    
    Args:
        collection: ChromaDB collection object
        ids: List of document IDs
        documents: List of document texts
        metadatas: Optional list of metadata dictionaries
        
    Raises:
        Exception: If data insertion fails
    """
    try:
        collection.add(
            ids=ids,
            documents=documents,
            metadatas=metadatas
        )
        logger.info(f"Inserted {len(ids)} document(s)")
    except Exception as e:
        logger.error(f"Failed to insert data: {e}")
        raise


if __name__ == "__main__":
    try:
        # Initialize client
        client = get_chroma_client()
        
        # Get or create collection
        collection = get_or_create_collection(client)
        
        # Insert sample data
        insert_sample_data(
            collection=collection,
            ids=["sample_1"],
            documents=["Dies ist ein Beispiel-Dokument für die Baseline."],
            metadatas=[{"type": "sample"}]
        )
        
        logger.info("Sample data insertion completed successfully")
        
    except Exception as e:
        logger.error(f"Failed to insert sample data: {e}")
        exit(1)