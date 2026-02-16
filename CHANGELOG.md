# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-02-16

### Added
- Initial baseline setup for ChromaDB
- Basic setup, insert, and query functionality
- Pretty-print utility for formatted output
- Centralized configuration management (`src/config.py`)
- Environment variable support via `.env` files
- Comprehensive logging throughout all modules
- Type hints for all functions (Python 3.8+ compatible)
- Exception handling in all modules
- Unit tests for `pretty_print` utility
- Development dependencies configuration (`requirements-dev.txt`)
- Linting configuration (`pyproject.toml`)
- Contributing guidelines (`CONTRIBUTING.md`)

### Fixed
- **CRITICAL**: Fixed duplicate `settings` argument in `src/setup/chroma_setup.py`
  - Previously, the second `settings` argument was overwriting the first
  - This caused telemetry disabling to be ignored
  - Now properly uses a single `settings` argument with correct configuration

### Changed
- Replaced `print()` statements with `logging` module
- Hardcoded paths now use environment variables with sensible defaults
- Collection names are now configurable via environment variables
- All modules now follow consistent error handling patterns
- Enhanced documentation with docstrings for all functions

### Technical Details
- Python 3.8+ compatibility maintained
- No breaking changes to existing functionality
- All new modules are fully documented
- Comprehensive test coverage for utility functions

## [Unreleased]

### Planned
- Additional unit tests for core functionality
- Integration tests for end-to-end workflows
- Performance benchmarks
- Extended documentation with usage examples
