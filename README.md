# Personal Finance API

## Project Environment Setup (using pyenv & pyenv-virtualenv)

1. Ensure you have `pyenv` and `pyenv-virtualenv` installed.
2. Install the required Python version (if not already installed):
   ```bash
   pyenv install 3.11.7
   ```
3. Create a virtual environment named `financial`:
   ```bash
   pyenv virtualenv 3.11.7 financial
   ```
4. Set the local Python version for this project:
   ```bash
   pyenv local financial
   ```
5. Activate the virtual environment (if not auto-activated):
   ```bash
   pyenv activate financial
   # or
   pyenv shell financial
   ```
6. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Definition Summary

A web API for users to manage their personal finances, register incomes and expenses, and receive budget and savings recommendations, with support for both manual and automated (API Key) data entry.

### Key Features

1. **User Registration & Profile**
   - Users register with: first name, last name, nickname, document type, document number, phone number, email, and password.
   - All fields and models are in English.

2. **Authentication**
   - JWT authentication for users (email & password).
   - API Key authentication for automated agents (e.g., AI reading emails/SMS).

3. **Base Income & Fixed Expenses**
   - Users enter their base monthly income (salary).
   - Users register their fixed/basic monthly expenses (e.g., rent, utilities, food).

4. **Savings Suggestion & Budget**
   - The system suggests saving at least 33% of the salary.
   - If the remaining amount after expenses is greater than 33%, the system suggests:
     - Minimum savings: 33% of salary.
     - Maximum savings: remaining amount after expenses.
   - Provides a budget summary: total income, total fixed expenses, suggested savings (min/max), available budget.

5. **Transactions**
   - All incomes and expenses are recorded as transactions.
   - Each transaction includes: type (income/expense), category, amount, date, description.

6. **Budget Compliance & Reporting**
   - The system tracks and reports, for each month, how much the user has actually saved vs. the suggested savings.
   - When a new transaction is registered, the system returns the current month's budget compliance and the full transaction history.

### Technical Notes

- All endpoints and models use English names.
- The system is ready for both manual and automated (API Key) data entry.
- Reports and compliance checks are available via API endpoints.

## Features

- User authentication and authorization
- Income and expense tracking
- Budget management
- Category management
- Transaction history

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file in the root directory with the following variables:
```
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## API Documentation

The API documentation will be available at `/api/docs/` when the server is running.

## Autenticación y Seguridad

### 1. Autenticación JWT (usuario/contraseña)
- Los usuarios humanos se registran y autentican usando email/usuario y contraseña.
- El sistema emite un token JWT para acceder a los endpoints protegidos.
- Permite acceso seguro y controlado a la API desde aplicaciones web o móviles.

### 2. Autenticación por API Key (para agentes automáticos)
- El sistema permite generar una o varias API Keys asociadas a un usuario.
- Un agente de IA (o cualquier sistema automatizado) puede usar la API Key para registrar ingresos y egresos automáticamente (por ejemplo, leyendo emails o SMS).
- Las API Keys pueden ser revocadas o regeneradas por el usuario.
- Los endpoints aceptan autenticación por API Key en los headers.
