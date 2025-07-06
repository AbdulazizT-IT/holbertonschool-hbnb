# HolbertonSchool HBNB - Part 2

This is a simple Flask-based REST API project.

## Project Structure

par2/
| Path                     | Description                                         |
|--------------------------|-----------------------------------------------------|
| `app/`                   | Main application package containing all app logic.  |
| `app/__init__.py`        | Initializes the app and sets up the app factory.    |
| `app/api/`               | Contains API route modules.                         |
| `app/api/v1/`            | Version 1 of the API endpoints.                     |
| `app/models/`            | Contains data model classes.                        |
| `app/services/`          | Business logic layer.                               |
| `app/persistence/`       | Handles data storage logic (repository pattern).    |
| `app/persistence/repository.py` | Implementation of in-memory repository.      |
| `config.py`              | Application configuration settings.                |
| `requirements.txt`       | Python dependencies file.                          |
| `run.py`                 | Entry point to start the Flask application.         |
| `README.md`              | Project documentation file.                         |


app/
| Path            | Description                                                  |
| --------------- | ------------------------------------------------------------ |
| `api/`          | Contains API route files for each resource (users, places, etc.). |
| `models/`       | Represents the objects or entities used in the system.       |
| `persistence/`  | Contains code for storing and retrieving data from memory.   |
| `services/`     | Contains the business logic of the application.              |


## Setup Instructions

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

2. **Run the application:**

python3 run.py


The app will start on http://127.0.0.1:5000

---

## ✍️ Author
[Abdulaziz - "AbdulazizT-IT"](https://github.com/AbdulazizT-IT)
[Yasser - "YuriSoma"](https://github.com/YuriSoma)
[Meshari - M0simi](https://github.com/M0simi)
