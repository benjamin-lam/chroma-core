"""
Module for raw query execution against ChromaDB.

This module provides functionality to query ChromaDB collections
and display results in raw format.
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
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
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
            ),
        )
        logger.info("ChromaDB client initialized")
        return client
    except Exception as e:
        logger.error(f"Failed to initialize ChromaDB client: {e}")
        raise


def get_collection(
    client: chromadb.PersistentClient, collection_name: Optional[str] = None
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
        logger.error(f"Failed to get collection: {e}")
        raise


def query_collection(
    collection: Collection, query_texts: List[str], n_results: int = 3
) -> Dict[str, Any]:
    """
    Query a ChromaDB collection.

    Args:
        collection: ChromaDB collection object
        query_texts: List of query text strings
        n_results: Number of results to return

    Returns:
        Dict[str, Any]: Query results

    Raises:
        Exception: If query execution fails
    """
    try:
        results = collection.query(query_texts=query_texts, n_results=n_results)
        logger.info(f"Query returned {len(results.get('ids', [[]])[0])} result(s)")
        return results
    except Exception as e:
        logger.error(f"Failed to query collection: {e}")
        raise


if __name__ == "__main__":
    try:
        # Initialize client
        client = get_chroma_client()

        # Get collection
        collection = get_collection(client)

        # Execute query
        results = query_collection(
            collection=collection, query_texts=["Beispiel"], n_results=3
        )

        # Display results
        logger.info("Query results:")
        print(results)

    except Exception as e:
        logger.error(f"Query execution failed: {e}")
        exit(1)
