# Django Game Project

This is a **small Django-based game** with an **API endpoint to save and retrieve scores**. The project demonstrates web development, containerization, and CI/CD automation.

---

## Technologies Used

* **Django** – Chosen for its simplicity in handling templates and static files, making web app development fast and efficient.

* **SQLite** – Lightweight database used to store scores; suitable since no sensitive or private data is required.

* **Docker** – Containerized the application to ensure it runs consistently across different environments.

* **GitHub/GitLab Workflows** – CI/CD pipeline implemented to automate building and deploying the Docker image whenever changes are pushed.


## CI/CD Automation
The project uses **GitHub Actions** to automate the deployment pipeline:
* **Trigger:** Every `push` to the `main` branch.
* **Process:** Automatically builds the Docker image and authenticates via secrets.
* **Deployment:** Pushes the latest build to [Docker Hub](https://hub.docker.com/r/leh3ch/test_django_game) as `leh3ch/test_django_game:latest`.

1. **Pull and Run the image:**
   ```bash
   docker run -p 8000:8000 leh3ch/test_django_game:latest

2. **Access the App:**
    Open your browser and go to: http://localhost:8000