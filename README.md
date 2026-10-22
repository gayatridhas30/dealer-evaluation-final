# Dealer Evaluation Django Application

## Project Overview
This is a Django-based dealership evaluation application that provides API endpoints for managing car dealers, reviews, and sentiment analysis. The application is containerized using Docker and can be deployed to Kubernetes clusters.

## Features
- User authentication (login/logout) with Django admin
- Dealer management (CRUD operations)
- Car make and model listings
- Review submission and sentiment analysis
- Filter dealers by state
- Role-based access

## Technology Stack
- Django 6.1.2
- Django REST Framework
- SQLite3 database
- Docker for containerization
- Kubernetes for orchestration

## API Endpoints
- GET /api/makes/ - List all car makes
- GET /api/dealers/ - List all dealers
- GET /api/dealers/?state=Kansas - Filter dealers by state
- GET /api/dealers/{id}/ - Get dealer by ID
- GET /api/reviews/ - List all reviews
- GET /api/reviews/?dealer_id={id} - Get reviews for a dealer
- POST /api/reviews/ - Submit a new review
- POST /admin/login/ - Admin login

## Containerization
- Dockerfile built and pushed to IBM Cloud Container Registry
- Kubernetes deployment.yaml created for dealership application
- Port forwarding used for local development (8000:8000)

## Installation
1. Clone the repository
2. Run `docker build -t us.icr.io/<namespace>/dealership .`
3. Run `docker push us.icr.io/<namespace>/dealership`
4. Apply deployment: `kubectl apply -f deployment.yaml`
5. Port-forward: `kubectl port-forward deployment.apps/dealership 8000:8000`