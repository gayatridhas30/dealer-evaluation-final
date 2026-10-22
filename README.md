# Dealership Evaluation Application

## Project Name: Dealership Evaluation Application

A full-stack Django web application for evaluating car dealers with user authentication, dealer management, reviews, and sentiment analysis. Containerized with Docker and deployed to Kubernetes.

## Technology Stack
- **Backend:** Django 6.1.2, Django REST Framework 3.18.3
- **Database:** SQLite3
- **Frontend:** HTML/CSS, Bootstrap 5, React (Register component)
- **Containerization:** Docker (python:3.12.0-slim-bookworm)
- **Orchestration:** Kubernetes (deployment.yaml with RollingUpdate strategy)
- **CI/CD:** GitHub Actions

## Project Structure
```
dealer-evaluation-final/
├── manage.py                    # Django management script
├── requirements.txt             # Python dependencies
├── Dockerfile                   # Container build instructions
├── entrypoint.sh                # Container startup script
├── deployment.yaml              # Kubernetes deployment manifest
├── deploymentURL                # Deployment URL file
├── CICD                         # GitHub Actions workflow output
├── README.md                    # Project documentation
├── djangoproj/                  # Django project settings
├── dealership/                  # Django app (models, views, API)
├── templates/                   # HTML templates
├── server/
│   └── frontend/
│       ├── static/
│       │   ├── About.html       # About Us page
│       │   └── Contact.html     # Contact Us page
│       └── src/
│           └── components/
│               └── Register/
│                   └── Register.jsx  # Sign-up component
└── frontend/                    # Additional frontend files
```

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/makes/ | List all car makes |
| GET | /api/dealers/ | List all dealers |
| GET | /api/dealers/?state=Kansas | Filter dealers by state |
| GET | /api/dealers/{id}/ | Get dealer by ID |
| GET | /api/dealers/{id}/reviews/ | Get reviews for a dealer |
| GET | /api/reviews/ | List all reviews |
| POST | /api/reviews/ | Submit a new review |
| POST | /api/reviews/analyze/ | Sentiment analysis |

## Setup & Run
```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

## Docker Build & Deploy
```bash
docker build -t us.icr.io/<namespace>/dealership .
docker push us.icr.io/<namespace>/dealership
kubectl apply -f deployment.yaml
kubectl port-forward deployment.apps/dealership 8000:8000
```

## Admin Credentials
- **Username:** root
- **Password:** admin123

## Author
Gayatri Dhas