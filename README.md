# B2Broker Test Task

This project implements a **Django REST Framework** application that provides a JSON:API-compliant REST API for managing wallets and transactions. The application includes support for filtering, pagination, sorting, and validation to ensure wallet balances never go negative.

---

## Features

- **Wallet Management**:
  - Create, retrieve, update, and delete wallets.
  - Automatically calculates wallet balances based on associated transactions.

- **Transaction Management**:
  - Create, retrieve, update, and delete transactions.
  - Ensures wallet balances are updated with each transaction.
  - Prevents negative wallet balances.

- **JSON:API Specification**:
  - Fully compliant with JSON:API, using `django-rest-framework-json-api`.

- **Pagination, Sorting, and Filtering**:
  - Supports filtering by wallet ID and transaction ID.
  - Sort wallets by balance and transactions by amount.
  - Pagination with configurable page sizes.

- **Validation**:
  - Enforces unique transaction IDs.
  - Prevents wallet balances from going negative.

---

## Prerequisites

- Docker and Docker Compose
- Python 3.11+
- Node.js (if needed for frontend integration)

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/b2broker_test_task.git
cd b2broker_test_task
```

2. Setup the Environment

Ensure Docker is installed and running on your system.

3. Start the Application

Using Docker Compose, start the application:

docker-compose up --build

The application will be available at http://localhost:8000.

4. Run Migrations

Ensure the database schema is up to date:

docker exec django-app python manage.py migrate

5. Create a Superuser (Optional)

To access the Django admin panel:

docker exec django-app python manage.py createsuperuser

API Endpoints

Wallet Endpoints

	•	List Wallets: GET /wallets/
	•	Retrieve Wallet: GET /wallets/<id>/
	•	Create Wallet: POST /wallets/
	•	Update Wallet: PATCH /wallets/<id>/
	•	Delete Wallet: DELETE /wallets/<id>/

Example Create Wallet Request:

POST /wallets/
Content-Type: application/vnd.api+json

{
  "data": {
    "type": "Wallet",
    "attributes": {
      "label": "My Wallet"
    }
  }
}

Transaction Endpoints

	•	List Transactions: GET /transactions/
	•	Retrieve Transaction: GET /transactions/<id>/
	•	Create Transaction: POST /transactions/
	•	Update Transaction: PATCH /transactions/<id>/
	•	Delete Transaction: DELETE /transactions/<id>/

Example Create Transaction Request:

POST /transactions/
Content-Type: application/vnd.api+json

{
  "data": {
    "type": "Transaction",
    "attributes": {
      "txid": "unique-txid-123",
      "amount": "100.00"
    },
    "relationships": {
      "wallet": {
        "data": {
          "type": "Wallet",
          "id": "1"
        }
      }
    }
  }
}

Running Tests

The project includes automated tests written using pytest.

Run All Tests

docker exec django-app pytest

Run Specific Tests

To run a specific test file:

docker exec django-app pytest tests/test_models.py

Environment Variables

The application uses the following environment variables, which can be configured in docker-compose.yml:

Variable	Default Value	Description
DB_HOST	db	Database host
DB_PORT	3306	Database port
DB_NAME	wallet_db	Database name
DB_USER	root	Database user
DB_PASSWORD	password	Database password
DEBUG	1	Enable Django debug mode (1 = true)

Development with VS Code

The project includes a .devcontainer configuration for development inside a container using VS Code.
	1.	Install the Remote - Containers extension in VS Code.
	2.	Open the project folder in VS Code.
	3.	When prompted, reopen the folder in the container.

Directory Structure

.
├── core/
│   ├── models.py       # Defines Wallet and Transaction models
│   ├── serializers.py  # Serializers for API responses
│   ├── views.py        # ViewSets for Wallets and Transactions
│   ├── urls.py         # API endpoint definitions
│   ├── tests/          # Contains unit tests for models and APIs
├── manage.py           # Django project management script
├── docker-compose.yml  # Docker Compose configuration
├── .devcontainer/      # VS Code Dev Container configuration
└── README.md           # Project documentation

Technologies Used

	•	Backend:
	•	Python 3.11
	•	Django REST Framework
	•	django-rest-framework-json-api
	•	MySQL
	•	Tools:
	•	Docker & Docker Compose
	•	pytest for testing
	•	drf-spectacular for OpenAPI schema generation

Future Improvements

	•	Add caching for frequently accessed wallet balances.
	•	Implement a frontend using React or Angular.
	•	Improve API response performance with database optimizations.
	•	Add CI/CD pipeline for automated testing and deployment.