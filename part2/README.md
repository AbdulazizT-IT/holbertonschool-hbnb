# HolbertonSchool HBNB - Part 2

This is a simple Flask-based REST API project.

## Project Structure

part2/
├── app/ # Application package
│ ├── init.py # App factory and initialization
│ ├── api/ # API routes
│ │ └── v1/ # Version 1 of the API
│ ├── models/ # Data models
│ ├── services/ # Business logic
│ └── persistence/ # Data storage and repository pattern
│ └── repository.py
├── config.py # Configuration settings
├── requirements.txt # Python dependencies
├── run.py # Entry point to run the app
└── README.md # This file

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
