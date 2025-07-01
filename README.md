# Assignment Demo

This repository contains a simple FastAPI application for storing and retrieving words using a PostgreSQL database. The project demonstrates modern API development, containerization, and CI/CD best practices.

## Prerequisites

- [Docker](https://www.docker.com/)
- [k3d](https://k3d.io/stable/#install-script)
- [Helm](https://helm.sh/docs/intro/install/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)

## Features
- **FastAPI** backend for high-performance APIs
- **PostgreSQL** database integration
- **Docker** and **docker-compose** for easy local development
- **GitHub Actions** for automated CI/CD and Docker image publishing
- **Postman collection** for easy API testing
- Developed with **GitHub Copilot**

## Local Development

Run:

```sh
docker compose up -d --build
```
- API: http://localhost:8000
- Docs: http://localhost:8000/docs

## Endpoints

- `PUT /word` — Add a word (JSON: `{ "word": "example" }`)
- `GET /words` — List all words

## API Testing

Import the provided `postman-test.postman_collection.json` file into Postman to test the endpoints.

## CI/CD

- On push to `main`, a Docker image is built and pushed to GitHub Container Registry using GitHub Actions.

---
