"""
Utility module for pretty-printing ChromaDB query results.

This module provides functions to format and display ChromaDB query results
in a readable JSON format.
"""
import json
import logging
from typing import Any, Dict


logger = logging.getLogger(__name__)


def pretty_print(results: Dict[str, Any]) -> None:
    """
    Display ChromaDB query results in a formatted manner.
    
    Args:
        results: Query results from ChromaDB
        
    Returns:
        None
    """
    try:
        formatted = json.dumps(results, indent=2, ensure_ascii=False, default=str)
        print(formatted)
    except (TypeError, ValueError) as e:
        logger.warning(f"Failed to format results as JSON: {e}")
        print("Raw results:")
        print(results)
    except Exception as e:
        logger.error(f"Unexpected error while formatting results: {e}")
        print("Raw results:")
        print(results)