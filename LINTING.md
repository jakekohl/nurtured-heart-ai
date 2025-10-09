# Linting Configuration

This project uses separate linting configurations for the backend (Python) and frontend (JavaScript/Vue).

## Backend (Python)

The backend uses [Ruff](https://github.com/astral-sh/ruff), a fast Python linter and formatter.

### Configuration
- **File**: `backend/pyproject.toml`
- **Indentation**: 2 spaces
- **Line length**: 100 characters
- **Rules**: Standard Python linting (pycodestyle, pyflakes, isort, pep8-naming, etc.)

### Installation
```bash
cd backend
pip install -r requirements.txt
```

### Usage
```bash
# Check for linting issues
cd backend
ruff check .

# Auto-fix linting issues
ruff check --fix .

# Check code formatting
ruff format --check .

# Auto-format code
ruff format .

# Or use the convenience script
./lint.sh
```

## Frontend (JavaScript/Vue)

The frontend uses [ESLint](https://eslint.org/) with Vue 3 support.

### Configuration
- **File**: `frontend/.eslintrc.json`
- **Indentation**: 2 spaces
- **Quote style**: Single quotes
- **Semicolons**: Not required
- **Rules**: Standard JavaScript + Vue 3 recommended rules

### Installation
```bash
cd frontend
npm install
```

### Usage
```bash
# Check for linting issues
cd frontend
npm run lint

# Auto-fix linting issues
npm run lint:fix
```

## Editor Integration

### VS Code
For the best experience, install these extensions:
- **Python**: Ruff extension (`charliermarsh.ruff`)
- **JavaScript/Vue**: ESLint extension (`dbaeumer.vscode-eslint`)

### Other Editors
Most modern editors support Ruff and ESLint. Check your editor's plugin marketplace.

## CI/CD Integration

You can add these commands to your CI/CD pipeline:

```bash
# Backend linting
cd backend && ruff check . && ruff format --check .

# Frontend linting
cd frontend && npm run lint
```

## Common Issues

### Backend
- **Import sorting**: Ruff automatically sorts imports. Run `ruff check --fix .` to fix.
- **Line too long**: Keep lines under 100 characters or split them.

### Frontend
- **Missing semicolons**: This project doesn't use semicolons. Remove them if ESLint complains.
- **Quotes**: Use single quotes for strings.
- **Indentation**: Use 2 spaces, not tabs.

