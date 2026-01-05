# GitHub Actions Workflows

## Test Workflow (`test.yml`)

Runs unit tests on push and pull requests to main/master/develop branches.

- Tests against Python 3.8, 3.9, 3.10, 3.11, and 3.12
- Installs dev dependencies and runs `make test`

## Publish Workflow (`publish.yml`)

Automatically publishes to PyPI when a GitHub release is created.

### Setup

1. Create a PyPI API token:
   - Go to https://pypi.org/manage/account/token/
   - Create a new API token with "Upload packages" scope

2. Add the token as a GitHub secret:
   - Go to your repository Settings → Secrets and variables → Actions
   - Add a new secret named `PYPI_API_TOKEN` with your PyPI API token

### Usage

1. Create a new release on GitHub:
   - Go to Releases → Draft a new release
   - Create a new tag (e.g., `v0.1.0` or `0.1.0`)
   - The workflow will automatically:
     - Extract the version from the tag
     - Update version in `atis_parser/__init__.py`, `pyproject.toml`, and `setup.py`
     - Build the package
     - Publish to PyPI

### Tag Format

The release tag can be in either format:
- `v0.1.0` (with 'v' prefix)
- `0.1.0` (without prefix)

Both will be normalized to `0.1.0` for the package version.

