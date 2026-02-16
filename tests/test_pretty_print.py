"""
Unit tests for the pretty_print utility module.

Tests the formatting and error handling of the pretty_print function.
"""

import json

from src.utils.pretty_print import pretty_print


class TestPrettyPrint:
    """Test suite for pretty_print function."""

    def test_pretty_print_with_valid_dict(self, capsys):
        """Test pretty_print with a valid dictionary."""
        test_data = {
            "ids": [["id1", "id2"]],
            "documents": [["doc1", "doc2"]],
            "metadatas": [[{"key": "value"}, {"key2": "value2"}]],
        }

        pretty_print(test_data)

        captured = capsys.readouterr()
        output = captured.out

        # Verify it's valid JSON
        parsed = json.loads(output)
        assert parsed == test_data

    def test_pretty_print_with_chromadb_results(self, capsys):
        """Test pretty_print with typical ChromaDB query results."""
        test_data = {
            "ids": [["sample_1"]],
            "documents": [["Dies ist ein Beispiel-Dokument für die Baseline."]],
            "metadatas": [[{"type": "sample"}]],
            "distances": [[0.0]],
        }

        pretty_print(test_data)

        captured = capsys.readouterr()
        output = captured.out

        # Verify formatting
        assert "sample_1" in output
        assert "Dies ist ein Beispiel-Dokument" in output
        assert '"type": "sample"' in output

    def test_pretty_print_with_special_characters(self, capsys):
        """Test pretty_print with special characters and unicode."""
        test_data = {"text": "Spëciål çhâråctérs: äöü ß", "emoji": "🎉 🚀"}

        pretty_print(test_data)

        captured = capsys.readouterr()
        output = captured.out

        # ensure_ascii=False should preserve unicode
        assert "äöü" in output
        assert "🎉" in output

    def test_pretty_print_with_non_serializable_object(self, capsys):
        """Test pretty_print with non-JSON-serializable objects."""

        class CustomObject:
            def __str__(self):
                return "CustomObject"

        test_data = {"object": CustomObject(), "value": 42}

        pretty_print(test_data)

        captured = capsys.readouterr()
        output = captured.out

        # Should use default=str to convert object
        assert "CustomObject" in output

    def test_pretty_print_with_empty_dict(self, capsys):
        """Test pretty_print with an empty dictionary."""
        test_data = {}

        pretty_print(test_data)

        captured = capsys.readouterr()
        output = captured.out

        assert "{}" in output

    def test_pretty_print_with_nested_structures(self, capsys):
        """Test pretty_print with deeply nested structures."""
        test_data = {"level1": {"level2": {"level3": {"data": "value"}}}}

        pretty_print(test_data)

        captured = capsys.readouterr()
        output = captured.out

        # Verify nested structure is formatted
        assert "level1" in output
        assert "level2" in output
        assert "level3" in output
        assert '"data": "value"' in output

    def test_pretty_print_handles_non_dict_gracefully(self, capsys):
        """Test that pretty_print handles non-dict input gracefully."""
        # Should still work with non-dict objects
        pretty_print([1, 2, 3])

        captured = capsys.readouterr()
        output = captured.out

        # Should output something (either formatted or raw)
        assert output.strip() != ""
