# Assignment_Project

A simple FastAPI application for managing addresses with CRUD operations and distance filtering.

## Features

- Create, Read, Update, and Delete addresses.
- Filter addresses based on distance from a given location.

## Requirements

- Python 3.6+
- FastAPI
- SQLAlchemy
- Geopy

## Installation

1. Clone the repository:

git clone https://github.com/yourusername/fastapi-address-management.git

css
Copy code

2. Navigate to the project directory:

cd fastapi-address-management



3. Install dependencies:

pip install -r requirements.txt



## Usage

1. Start the FastAPI server:

uvicorn main:app --reload



2. Access the FastAPI interactive documentation:

Open a web browser and go to http://localhost:8000/docs.

## API Endpoints

- POST /addresses/: Create a new address.
- GET /addresses/{address_id}: Retrieve an address by ID.
- PUT /addresses/{address_id}: Update an address by ID.
- DELETE /addresses/{address_id}: Delete an address by ID.
- POST /addresses/distance/: Get addresses within a certain distance from a location.

## Configuration

You can configure the SQLite database connection by modifying the SQLALCHEMY_DATABASE_URL in db/database.py.
