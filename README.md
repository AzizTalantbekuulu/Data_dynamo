# DataDynamo Technologies Data Analytics Platform

DataDynamo Technologies is a data-driven startup focused on developing scalable and efficient back-end solutions for data processing and analysis.

## Project Overview

This project aims to design and implement a scalable back-end system for DataDynamo Technologies' data analytics platform. The system is capable of processing large volumes of data efficiently and performing complex analytical tasks.

## Features

- User management: CRUD operations for managing users.
- Event tracking: Record and manage user events.
- Data management: Upload, manage, and analyze data.
- Analysis: Perform text data analysis.
- API endpoints: Expose CRUD operations via RESTful APIs.

## Technologies Used

- Python
- Django
- Django REST Framework
- NLTK (Natural Language Toolkit)

## Getting Started

1. Clone the repository: `git clone https://github.com/your-username/data-analytics-platform.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Apply database migrations: `python manage.py migrate`
4. Run the development server: `python manage.py runserver`

## Usage

- Access the Django admin panel at `http://localhost:8000/admin/` to manage users, events, and data.
- Use API endpoints to interact with the system programmatically.
- Analyze text data by sending a POST request to `http://localhost:8000/analytics/analysis/` with the data ID.

## Contributors

- Abdulaziz Talantbek uulu (Abdulaziz.talantbekuulu@alatoo.edu.kg)

## API Endpoints

### Users

- **List Users:** `GET /users/`
- **Retrieve User:** `GET /users/{id}/`
- **Create User:** `POST /users/`
- **Update User:** `PUT /users/{id}/`
- **Delete User:** `DELETE /users/{id}/`

### Events

- **List Events:** `GET /events/`
- **Retrieve Event:** `GET /events/{id}/`
- **Create Event:** `POST /events/`
- **Update Event:** `PUT /events/{id}/`
- **Delete Event:** `DELETE /events/{id}/`

### Data

- **List Data:** `GET /data/`
- **Retrieve Data:** `GET /data/{id}/`
- **Create Data:** `POST /data/`
- **Update Data:** `PUT /data/{id}/`
- **Delete Data:** `DELETE /data/{id}/`

### Analysis

- **Analyze Text Data:** `POST /analysis/`

   *Body Parameters:*
   ```json
   {
       "data_id": 1
   }
