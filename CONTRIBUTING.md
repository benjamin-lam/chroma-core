# Contributing to Chroma Core

Thank you for your interest in contributing to Chroma Core! This document provides guidelines and instructions for contributing to this project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Project Structure](#project-structure)
- [Making Changes](#making-changes)
- [Testing](#testing)
- [Code Quality](#code-quality)
- [Submitting Changes](#submitting-changes)
- [Feature Branches](#feature-branches)

## Code of Conduct

This project follows a simple code of conduct:

- Be respectful and inclusive
- Provide constructive feedback
- Focus on what is best for the community
- Show empathy towards other contributors

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally
3. Set up the development environment
4. Create a new branch for your changes
5. Make your changes
6. Test your changes
7. Submit a pull request

## Development Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git

### Initial Setup

```bash
# Clone the repository
git clone https://github.com/<your-username>/chroma-core
cd chroma-core

# Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install production dependencies
pip install -r requirements.txt

# Install development dependencies
pip install -r requirements-dev.txt

# Set up environment variables (optional)
cp .env.example .env
# Edit .env with your preferred settings
```

## Project Structure

```
chroma-core/
├── src/                      # Source code
│   ├── setup/               # Setup scripts
│   ├── insert/              # Data insertion modules
│   ├── query/               # Query modules
│   ├── utils/               # Utility functions
│   └── config.py            # Configuration management
├── tests/                   # Unit tests
├── docs/                    # Documentation
├── data/                    # Data files (gitignored)
├── requirements.txt         # Production dependencies
├── requirements-dev.txt     # Development dependencies
├── pyproject.toml          # Project and tool configuration
├── CHANGELOG.md            # Version history
└── README.md               # Project overview
```

## Making Changes

### Branching Strategy

- `main` - Stable baseline code
- `feature/<name>` - New features
- `fix/<name>` - Bug fixes
- `docs/<name>` - Documentation improvements

### Coding Standards

1. **Python Version**: Code must be compatible with Python 3.8+
2. **Type Hints**: Use type hints for all function signatures
3. **Docstrings**: All functions and classes must have docstrings
4. **Logging**: Use the `logging` module instead of `print()`
5. **Error Handling**: Include appropriate exception handling
6. **Configuration**: Use `src/config.py` for configurable values

### Code Style

This project uses:
- **Black** for code formatting (line length: 88)
- **Flake8** for linting
- **mypy** for type checking

```bash
# Format code
black src/ tests/

# Run linter
flake8 src/ tests/

# Type check
mypy src/
```

## Testing

### Writing Tests

- Place tests in the `tests/` directory
- Name test files as `test_<module>.py`
- Use pytest for testing
- Aim for high test coverage

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=src --cov-report=term-missing

# Run specific test file
pytest tests/test_pretty_print.py

# Run tests in verbose mode
pytest -v
```

## Code Quality

Before submitting changes, ensure:

1. **All tests pass**: `pytest`
2. **Code is formatted**: `black src/ tests/`
3. **Linting passes**: `flake8 src/ tests/`
4. **Type checking passes**: `mypy src/`
5. **No secrets or credentials in code**

### Pre-commit Checklist

- [ ] All tests pass
- [ ] Code is formatted with Black
- [ ] Flake8 reports no errors
- [ ] Type hints are present and correct
- [ ] Docstrings are complete
- [ ] CHANGELOG.md is updated (if applicable)
- [ ] No breaking changes (or clearly documented)

## Submitting Changes

### Pull Request Process

1. **Update documentation**: Ensure README, docstrings, and CHANGELOG are current
2. **Test thoroughly**: All existing tests must pass
3. **Add tests**: New features should include tests
4. **Describe changes**: Provide a clear PR description
5. **Reference issues**: Link related issues in the PR

### Pull Request Template

```markdown
## Description
Brief description of the changes

## Type of Change
- [ ] Bug fix (non-breaking change fixing an issue)
- [ ] New feature (non-breaking change adding functionality)
- [ ] Breaking change (fix or feature causing existing functionality to change)
- [ ] Documentation update

## Testing
Describe the tests you ran and how to reproduce them

## Checklist
- [ ] Code follows project style guidelines
- [ ] All tests pass
- [ ] Documentation updated
- [ ] CHANGELOG.md updated
- [ ] No breaking changes (or documented)
```

## Feature Branches

### Adding New Features

When adding features (e.g., e-commerce seasonal brain, project truth):

1. **Create feature branch**: `git checkout -b feature/<feature-name>`
2. **Organize by feature**:
   ```
   data/<feature-name>/           # Feature-specific data
   src/insert/<feature-name>/     # Feature insert scripts
   src/query/<feature-name>/      # Feature query scripts
   docs/features/<feature-name>.md # Feature documentation
   ```
3. **Maintain compatibility**: Don't break existing functionality
4. **Document thoroughly**: Add feature documentation in `docs/features/`

### Example Feature Structure

```
feature/seasonal-brain/
├── data/seasonal-brain/
│   └── products.json
├── src/insert/seasonal-brain/
│   └── insert_products.py
├── src/query/seasonal-brain/
│   └── query_seasonal.py
└── docs/features/seasonal-brain.md
```

## Questions or Issues?

- Open an issue on GitHub for bugs or feature requests
- Check existing issues before creating new ones
- Provide as much context as possible

## License

By contributing, you agree that your contributions will be licensed under the same license as the project (MIT License).

## Recognition

Contributors will be recognized in the project documentation and release notes.

Thank you for contributing to Chroma Core! 🚀
